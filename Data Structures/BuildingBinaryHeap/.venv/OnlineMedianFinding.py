import BinaryHeap

class OnlineMedianFinding:
    def __init__ (self):
        self.large = BinaryHeap.BinaryHeap()
        self.small = BinaryHeap.BinaryHeap()
    
    def insert(self, value: int):
        #if the heap is empty, insert the value into the large heap
        if self.heap_size() == 0:
            self.large.insert(value)
            return
            
        #if the inserted value is greater than min of large, insert onto large
        if value >= self.large.find_min():
            self.large.insert(value)  
        else: #if not, insert onto small heap
            self.small.insert(-value) 
            
        #balance the heaps
        if self.large.size() - self.small.size() >= 2:
            self.small.insert(-self.large.remove_min())
        elif self.small.size() - self.large.size() >= 2:
            self.large.insert(-self.small.remove_min())

    def find_median(self):
        #if the heaps are the same size, return the average of the min of large and max of small
        if self.large.size() == self.small.size(): 
            return (self.large.find_min() - self.small.find_min()) / 2
        #if the size of large heap is greater, return the min of large
        elif self.large.size() > self.small.size():
            return self.large.find_min()
        #if the size of small heap is greater, return the max of small
        else:
            return -self.small.find_min()

    def heap_size(self):
        return self.large.size() + self.small.size()
    


def main():
    #main method writes the medians of the input file to the write file
    #the ouput file is the expected output of the input file
    input_file = ".venv\test-02-input.txt"  
    output_file = ".venv\test-02-write.txt" 

    median_finder = OnlineMedianFinding()

    
    input_file = ".venv/test-02-input.txt" 
    output_file = ".venv/test-02-write.txt"  

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            command = line.strip()
            if command.startswith("i"):
                _, value = command.split()
                median_finder.insert(int(value))
            elif command == "q":
                median = median_finder.find_median()
                outfile.write(f"{median}\n")
            elif command == "e":
                break


if __name__ == "__main__":
    main()
    
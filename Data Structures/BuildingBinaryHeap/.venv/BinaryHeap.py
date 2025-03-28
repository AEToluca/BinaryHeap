class BinaryHeap:
    def __init__(self):
        self.heap_list = []
        

    def insert(self, value):
            #add value to the end then sift up
            self.heap_list.append(value)
            self.sift_up()

    def remove_min(self) -> int:
        #raise an exception if the heap is empty
        if self.size() <= 0:
            return float('inf')
        if self.size() == 1:
            return self.heap_list.pop()
            
        min_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop() #return removed min
        self.sift_down()
        return min_val

    def sift_up(self):
        #set current to the last index
        current = self.size() - 1
        while current > 0: #go until current is root
            parent = (current - 1) // 2
            #swap if parent is greater than current
            if self.heap_list[parent] > self.heap_list[current]:
                self.heap_list[parent], self.heap_list[current] = self.heap_list[current], self.heap_list[parent]
                current = parent
            else:
                break

    def sift_down(self):
        #return if the heap is empty or has only one element
        if self.size() <= 1:
            return
            
        current = 0
        while True:
            #create variables for the current left and right children
            smallest = current
            left = 2 * current + 1
            right = 2 * current + 2
            
            #check if left or right child is smaller than the current
            if left < self.size() and self.heap_list[left] < self.heap_list[smallest]:
                smallest = left
                
            #check if right child is smaller than the current
            if right < self.size() and self.heap_list[right] < self.heap_list[smallest]:
                smallest = right
                
            #if the smallest is the current, break
            if smallest == current:
                break
                
            #swap the current with the smallest child
            self.heap_list[current], self.heap_list[smallest] = self.heap_list[smallest], self.heap_list[current]
            current = smallest

    #return the root node
    def find_min(self) -> int:
        if self.size() <= 0:
            return float('inf')
        return self.heap_list[0]

    #return the size of the heap
    def size(self) -> int:
        return len(self.heap_list)
    


def  main():
    test = BinaryHeap() 
    test.insert(7)
    test.insert(4)
    test.insert(5)
    test.insert(1)
    test.insert(3)
    print(test.remove_min())
    print(test.find_min())

if __name__ == "__main__":
    # Driver code to test your heap
    main()

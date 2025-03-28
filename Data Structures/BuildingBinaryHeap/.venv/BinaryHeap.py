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
            raise ("Heap is empty")
        else:
            #swap the first and last elements, put last element in a variable,sift down and return the variable
            self.heap_list[self.size() - 1], self.heap_list[0] = self.heap_list[0], self.heap_list[self.size() - 1]
            result = self.heap_list.pop()
            self.sift_down()
            return result
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
        #return if heap only has 1 or less elements
        if self.size() <= 1:
            return
        last = self.size() - 1
        #swap first and last items
        self.heap_list[0], self.heap_list[last] = self.heap_list[last], self.heap_list[0]

        current = 0
        while True:
            smallest = current
            left = 2 * current + 1
            right = 2 * current + 2

            #compare the left and last index to make sure we don't compare something out of range
            #compare the smallest node with the left child and swap if necessary
            if left < last and self.heap_list[left] < self.heap_list[smallest]:
                smallest = left

            if right < last and self.heap_list[right] < self.heap_list[smallest]:
                smallest = right

            if smallest == current:
                break

            self.heap_list[current], self.heap_list[smallest] = self.heap_list[smallest], self.heap_list[current]
            current = smallest
    #return the root node
    def find_min(self) -> int:
        return self.heap_list[0]

    #reutrn the size of the heap
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

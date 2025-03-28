class BinaryHeap:
    def __init__(self):
        self.heap_list = []
        

    def insert(self, value):
            self.heap_list.append(value)
            self.sift_up()

    def remove_min(self) -> int:
        pass

    def sift_up(self):
        
        current = self.size() - 1
        while current > 0:
            parent = (current - 1) // 2

            if self.heap_list[parent] > self.heap_list[current]:
                self.heap_list[parent], self.heap_list[current] = self.heap_list[current], self.heap_list[parent]
                current = parent
            else:
                break
    def sift_down(self):
        #return if heap only has 1 or less elements
        if self.size <= 1:
            return
        last = self.size()
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

    def find_min(self) -> int:
        return self.heap_list[0]

    def size(self) -> int:
        return len(self.heap_list)

    def isFull(self) -> bool:
        return True

def  main():
    test = BinaryHeap() 
    test.insert(4)
    test.insert(5)
    test.insert(2)
   
    test.insert(3)
    print(test.find_min())
    print(test.size())

if __name__ == "__main__":
    # Driver code to test your heap
    main()

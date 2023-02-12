class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    def parent_i(self, i):
        return i // 2

    def left_child_i(self, i):
        return i * 2

    def right_child_i(self, i):
        return i * 2 + 1

    def child_present(self, i):
        return self.left_child_i(i) <= self.count
    # END OF HEAP HELPER METHODS
      
    def add(self, element):
        self.count += 1
        print(f"Adding: {element} to {self.heap_list}")
        self.heap_list.append(element)
        self.heapify_up()
        
    def heapify_up(self):
        print("Heapifying up")
        i = self.count
        while self.parent_i(i) > 0:
            child = self.heap_list[i]
            parent = self.heap_list[self.parent_i(i)]
            if parent < child:
                print(f"Swapping {parent} with {child}")
                self.heap_list[i] = parent
                self.heap_list[self.parent_i(i)] = child
            i = self.parent_i(i)
        print(f"Heap Restored {self.heap_list}")

    def retrieve_max(self):
        if self.count == 0:
            print('No items in heap')
            return None
        max_val = self.heap_list[1]
        print(f'Removing: {max_val} from {self.heap_list}')
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print(f"Last element moved to first: {self.heap_list}")
        self.heapify_down()
        return max_val

    def heapify_down(self):
        print('Heapifying down!')
        i = 1
        while self.child_present(i):
            print('Heapifying down!')
            larger_child_i = self.get_larger_child_i(i)
            child = self.heap_list[larger_child_i]
            parent = self.heap_list[i]
            if parent < child:
                self.heap_list[i] = child
                self.heap_list[larger_child_i] = parent
            i = larger_child_i
            print(f'HEAP RESTORED! {self.heap_list}')

    def get_larger_child_i(self, i):
        if self.right_child_i(i) > self.count:
            print('There is only a left child')
            return self.left_child_i(i)
        else:
            left_child = self.heap_list[self.left_child_i(i)]
            right_child = self.heap_list[self.right_child_i(i)]
            if left_child > right_child:
                print(f'Left child {left_child} is larger than right child {right_child}')
                return self.left_child_i(i)
            else:
                print(f'Right child {right_child} is larger than left child {left_child}')
                return self.right_child_i(i)
"""
# TESTING
# import random number generator
from random import randrange

# make an instance of MaxHeap
max_heap = MaxHeap()

# populate max_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for n in random_nums:
    max_heap.add(n)
"""
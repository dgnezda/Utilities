def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iteration_count = 0
  
    for el in arr:
      
        for index in range(len(arr) - 1):
            iteration_count += 1
      
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)

    print(f"PRE-OPTIMIZED ITERATION COUNT: {iteration_count}")


def bubble_sort(arr):
    iteration_count = 0
      
    for i in range(len(arr)):
        
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            iteration_count += 1
        
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            
    print(f"POST-OPTIMIZED ITERATION COUNT: {iteration_count}")


# For testing purpouses:
if __name__ == "__main__":
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"PRE SORT: {nums}")

    bubble_sort_unoptimized(nums.copy())
    bubble_sort(nums)
    print(f"POST SORT: {nums}")
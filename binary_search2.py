def binary_search(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "Value not found"
        
    # Calculate the middle index from the pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    
    if mid_val > target:
        # reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    
    if mid_val < target:
        # reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
target = 288
result = binary_search(values, start_of_values, end_of_values, target)

print(f"Value {target} found at index {result}")
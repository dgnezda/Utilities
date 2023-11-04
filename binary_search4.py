def binary_search(sorted_list, target, left_pointer, right_pointer):
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
        return binary_search(sorted_list, target, left_pointer, mid_idx)
    
    if mid_val < target:
        # reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, target, mid_idx + 1, right_pointer)


# For testing purpouses  
if __name__ == "__main__":
    values = [77, 80, 102, 123, 288, 300, 540]
    start_of_values = 0
    end_of_values = len(values)
    target = 288
    
    result = binary_search(values, target, start_of_values, end_of_values)

    print(f"Value {target} found at index {result}")
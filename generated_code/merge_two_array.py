def merge_two_array(arr1, arr2):
    """
    This function merges two arrays and returns the merged array
    """
    merged_array = arr1 + arr2
    return merged_array


# Test cases
print(merge_two_array([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(merge_two_array([], [4, 5, 6]))  # Output: [4, 5, 6]
print(merge_two_array([1, 2, 3], []))  # Output: [1, 2, 3]
print(merge_two_array([], []))  # Output: []

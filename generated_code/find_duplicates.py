def find_duplicates(arr):
    duplicates = []
    for i in arr:
        if arr.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates


# Tests
print(find_duplicates([1, 2, 3, 4, 5]))  # Expected output: []
print(find_duplicates([1, 2, 3, 2, 5]))  # Expected output: [2]
print(find_duplicates([1, 1, 3, 3, 5]))  # Expected output: [1, 3]
print(find_duplicates([]))  # Expected output: []

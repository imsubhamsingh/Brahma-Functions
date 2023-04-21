def merge_two_linkedlists_v1(l1, l2):
    # Initialize a new linked list
    merged_list = None

    # Check if either list is empty
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    # Compare the first elements of each list
    if l1.data <= l2.data:
        merged_list = l1
        merged_list.next = merge_two_linkedlists_v1(l1.next, l2)
    else:
        merged_list = l2
        merged_list.next = merge_two_linkedlists_v1(l1, l2.next)

    return merged_list

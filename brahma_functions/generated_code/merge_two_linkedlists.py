def merge_two_linkedlists(l1, l2):
    # Create a placeholder for the result
    result_head = None
    current = None

    # Check if either list is empty
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return l2
    elif l2 is None:
        return l1

    # Compare the first element of each list
    if l1.val <= l2.val:
        result_head = l1
        current = l1
        l1 = l1.next
    else:
        result_head = l2
        current = l2
        l2 = l2.next

    # Iterate through both lists, adding the smaller
    # element to the result list, until one list is empty
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            current = l1
            l1 = l1.next
        else:
            current.next = l2
            current = l2
            l2 = l2.next

    # If one list is empty, append the other to the end of the result list
    if l1 is None:
        current.next = l2
    else:
        current.next = l1

    # Return the head of the merged list
    return result_head

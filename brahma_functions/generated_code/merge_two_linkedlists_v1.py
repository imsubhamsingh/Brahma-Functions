def merge_two_linkedlists_v1(l1, l2):
    # Create a new linked list
    merged_list = ListNode(None)
    # Create a reference to the head of the newly created list
    head = merged_list
    # Iterate through both linked lists
    while l1 and l2:
        # Compare the data of the nodes in the two linked lists
        if l1.data <= l2.data:
            # Add the node from l1 to the new list
            merged_list.next = l1
            # Move the pointer for l1 to the next node
            l1 = l1.next
        else:
            # Add the node from l2 to the new list
            merged_list.next = l2
            # Move the pointer for l2 to the next node
            l2 = l2.next
        # Move the pointer for the newly created list
        merged_list = merged_list.next
    # Add the remaining nodes from l1 or l2
    merged_list.next = l1 or l2
    # Return the head of the newly created list
    return head.next

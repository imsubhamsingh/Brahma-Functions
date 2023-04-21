def merge_two_linkedlists_v2(l1, l2):
    # set a pointer to the first node in l1
    current = l1.head

    # loop through the l2 list
    while l2.head:
        # save the next node in the l2 list
        next_node = l2.head.next

        # set the l2 list's head to the current l1 node
        l2.head.next = current.next

        # set the l1 node's next to the l2 list's head
        current.next = l2.head

        # set the current l1 node to the next node in l2
        current = current.next

        # set the l2 list's head to the next node in l2
        l2.head = next_node

    # return the l1 list
    return l1

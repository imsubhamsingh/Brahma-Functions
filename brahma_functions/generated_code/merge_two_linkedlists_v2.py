def merge_two_linkedlists_v2(l1, l2):
    """This function merges two linked lists together"""

    # create a new linked list
    merged_list = LinkedList()

    # create 2 variables to track the current nodes in each list
    cur_l1 = l1.head
    cur_l2 = l2.head

    # loop through the lists until one is empty
    while cur_l1 and cur_l2:
        # compare the values of the two nodes
        if cur_l1.data <= cur_l2.data:
            # if l1 is smaller, add it to the merged list
            merged_list.append(cur_l1.data)
            # move to the next node in l1
            cur_l1 = cur_l1.next
        else:
            # if l2 is smaller, add it to the merged list
            merged_list.append(cur_l2.data)
            # move to the next node in l2
            cur_l2 = cur_l2.next

    # if one list is not empty, add the rest of the elements to the merged list
    while cur_l1:
        merged_list.append(cur_l1.data)
        cur_l1 = cur_l1.next
    while cur_l2:
        merged_list.append(cur_l2.data)
        cur_l2 = cur_l2.next

    # return the merged list
    return merged_list

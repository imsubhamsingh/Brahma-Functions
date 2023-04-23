def merge_two_linkedlists_v2(l1, l2):
    """This function merges two linked lists together

    Args:
        l1: the first linked list
        l2: the second linked list

    Returns:
        the merged linked list
    """

    # Create a new linked list to store the merged list
    merged_list = LinkedList()

    # Iterate through both lists and add the nodes to the merged list
    curr_node_l1 = l1.head
    curr_node_l2 = l2.head

    while curr_node_l1 is not None and curr_node_l2 is not None:
        if curr_node_l1.data <= curr_node_l2.data:
            merged_list.append(curr_node_l1.data)
            curr_node_l1 = curr_node_l1.next
        else:
            merged_list.append(curr_node_l2.data)
            curr_node_l2 = curr_node_l2.next

    # Add the rest of the nodes from the longer list
    while curr_node_l1 is not None:
        merged_list.append(curr_node_l1.data)
        curr_node_l1 = curr_node_l1.next

    while curr_node_l2 is not None:
        merged_list.append(curr_node_l2.data)
        curr_node_l2 = curr_node_l2.next

    return merged_list

def merge_two_linkedlists_v1(l1, l2):
    # Create a pointer to traverse the lists
    current1 = l1
    current2 = l2

    # Create a new linked list to store the merged list
    merged_list = LinkedList()

    # Traverse both lists
    while current1 != None and current2 != None:
        # Compare the elements of the two lists
        if current1.data <= current2.data:
            # Add the smaller element to the merged list
            merged_list.append(current1.data)
            # Move the pointer to the next node
            current1 = current1.next
        else:
            # Add the smaller element to the merged list
            merged_list.append(current2.data)
            # Move the pointer to the next node
            current2 = current2.next

    # Check if either of the lists is left
    while current1 != None:
        # Add the remaining elements of l1 to the merged list
        merged_list.append(current1.data)
        # Move the pointer to the next node
        current1 = current1.next
    while current2 != None:
        # Add the remaining elements of l2 to the merged list
        merged_list.append(current2.data)
        # Move the pointer to the next node
        current2 = current2.next

    # Return the merged list
    return merged_list

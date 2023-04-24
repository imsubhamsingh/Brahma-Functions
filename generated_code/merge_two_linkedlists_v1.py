def merge_two_linkedlists_v1(l1, l2):
    """
    This function merges two linked lists together.

    Parameters:
    l1 (list): A linked list
    l2 (list): A linked list

    Returns:
    list: A merged list
    """

    # Create a new list for the merged list
    merged_list = []

    # Get the length of l1 and l2
    l1_length = len(l1)
    l2_length = len(l2)

    # Iterate until one of the lists is empty
    while l1_length > 0 and l2_length > 0:
        # Check if the element in l1 is less than the element in l2
        if l1[0] < l2[0]:
            # Remove the first element from l1 and append it to merged_list
            merged_list.append(l1.pop(0))
            l1_length -= 1
        else:
            # Remove the first element from l2 and append it to merged_list
            merged_list.append(l2.pop(0))
            l2_length -= 1

    # Append the remaining elements from l1 or l2 to the merged list
    if l1:
        merged_list.extend(l1)
    elif l2:
        merged_list.extend(l2)

    return merged_list


def test_merge_two_linkedlists_v1():
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]

    result = merge_two_linkedlists_v1(l1, l2)

    assert expected == result


test_merge_two_linkedlists_v1()

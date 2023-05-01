# Node class to create linked list nodes
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_linkedlists_v2(l1, l2):
    # Dummy node to start the merged linked list
    dummy = Node(0)
    # Pointer to keep track of the node to add to the merged linked list
    tail = dummy

    # Traverse both linked lists while they are not None
    while l1 and l2:
        # Choose the smaller value between the two lists and add it to the merged linked list
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Add any remaining nodes from the first linked list to the merged linked list
    if l1:
        tail.next = l1
    # Add any remaining nodes from the second linked list to the merged linked list
    if l2:
        tail.next = l2

    # Return the merged linked list
    return dummy.next


# Test cases
# Case 1: l1 and l2 are empty
# Expected output: None
l1 = None
l2 = None
print(merge_two_linkedlists_v2(l1, l2))

# Case 2: l1 is empty
# Expected output: l2 is the merged linked list
# 1 -> 2 -> 3 -> 4 -> 5
l1 = None
l2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
merged = merge_two_linkedlists_v2(l1, l2)
while merged:
    print(merged.val, end=" ")
    merged = merged.next

# Case 3: l2 is empty
# Expected output: l1 is the merged linked list
# 1 -> 2 -> 3 -> 4 -> 5
l1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
l2 = None
merged = merge_two_linkedlists_v2(l1, l2)
while merged:
    print(merged.val, end=" ")
    merged = merged.next

# Case 4: l1 and l2 have different values
# Expected output: merged linked list is in ascending order
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
l1 = Node(1, Node(3, Node(5, Node(7, Node(9)))))
l2 = Node(2, Node(4, Node(6, Node(8))))
merged = merge_two_linkedlists_v2(l1, l2)
while merged:
    print(merged.val, end=" ")
    merged = merged.next

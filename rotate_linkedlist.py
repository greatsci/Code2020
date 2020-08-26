# Given a linked list, how to right shift it by k nodes?
# Example
# Input:    1->2->3->4->5->Null, k = 2
# Output:   4->5->1->2->3->Null

# ------------------------------------------

class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3


def length(head):
    if not head:
        return 0
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count
# -----------------------------------------------------


def rotate_linkedlist(head, k):
    k = k % length(head)
    pos = length(head) - k
    tail = head
    for step in range(pos):
        tail = tail.next
    new_head = tail
    # Find and connect the original tail to original head
    curr = new_head
    while curr and curr.next:
        curr = curr.next
    curr.next = head
    return new_head
# T:O(n) S:O(1)

# Test
rl = rotate_linkedlist(node1, 1)
print(rl.val)

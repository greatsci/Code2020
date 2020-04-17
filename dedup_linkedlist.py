# Given a sorted linked list, how to delete duplicates and keep a copy of each value?
# Input:    1->1->1->2->2->3->3->3->Null
# Output:   1->2->3->Null


# ------------------------------------------------------
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
# -----------------------------------------------------


def dedup_linkedlist(head):
    curr = head
    tail = head
    fakehead = ListNode(None)
    fakehead.next = tail
    while curr:
        if curr.val == tail.val:
            curr = curr.next
        else:
            tail.next = curr
            tail = tail.next
    return fakehead.next
# T:O(n) S:O(1)

# Test
head = dedup_linkedlist(node1)
print(head.next.val)
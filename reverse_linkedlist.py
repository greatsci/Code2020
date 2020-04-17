# Reverse a linked list


class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


def reverse_linkedlist(head):
    if not head:
        return None
    if head.next is None:
        return head
    else:
        newhead = reverse_linkedlist(head.next)
        head.next.next = head
        head.next = None
        return newhead
# T:O(n) S:O(n)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Test
rl = reverse_linkedlist(node1)
print(rl.val)
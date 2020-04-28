# Reverse a linked list pair by pair
# Example
#   Input:  1->2->3->4->5->Null
#   Output: 2->1->4->3->5->Null

def paired_reverse_linkedlist(head):
    if head is None or head.next is None:
        return head
    newhead = head.next
    remain = paired_reverse_linkedlist(head.next.next)
    head.next.next = head
    head.next = remain
    return newhead
# T:O(n)    S:O(n)

# --------------------------------------------------
class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# Test
print('Before\n')
head = node1
for i in range(3):
    print(head.val)
    head = head.next

print('After\n')
newhead = paired_reverse_linkedlist(node1)
head = newhead
for i in range(3):
    print(head.val)
    head = head.next

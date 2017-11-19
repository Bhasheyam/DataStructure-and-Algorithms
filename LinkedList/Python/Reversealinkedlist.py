'''
Reverse a linked list. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.
'''
def reverseList(A):
    prev = None
    temp = None
    current = A
    while current:
        temp = current.next
        current.next = prev
        prev = current 
        current = temp
    A = prev
    return A
        
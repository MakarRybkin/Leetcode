from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer=head
        if head is None:
            return None
        while pointer is not None and pointer.next is not None:
            if pointer.val==pointer.next.val:
                pointer.next=pointer.next.next
            else:
                pointer=pointer.next
        return head

print(Solution().deleteDuplicates(ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))))
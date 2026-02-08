from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_rang=0
        result=ListNode()
        pointer=result
        while l1 is not None or l2 is not None:
            if l1 and l2:
                number = next_rang+l1.val+l2.val
                pointer.val=number%10
                next_rang=number//10
                l1=l1.next
                l2=l2.next
            elif l1 and l2 is None:
                pointer.val=(next_rang+l1.val)%10
                next_rang=(next_rang+l1.val)//10
                l1=l1.next
            elif l1 is None and l2 :
                pointer.val=(next_rang+l2.val)%10
                next_rang=(next_rang+l2.val)//10
                l2=l2.next
            if l1 or l2 :
                pointer.next=ListNode()
                pointer=pointer.next
        if next_rang!=0:
            pointer.next=ListNode(next_rang)
        return result
print(Solution().addTwoNumbers(l1=ListNode(2,next=ListNode(4,next=ListNode(3))), l2=ListNode(5,next=ListNode(6,next=ListNode(4)))))



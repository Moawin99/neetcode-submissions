# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        remainder = 0
        hm = {}
        c1, c2 = l1, l2

        while c1 or c2 or remainder != 0:
            newVal = 0
            if c1 and c2:
                newVal = c1.val + c2.val + remainder
                c1 = c1.next
                c2 = c2.next
            elif not c1 and c2:
                newVal =  c2.val + remainder
                c2 = c2.next
            elif not c2 and c1:
                newVal =  c1.val + remainder
                c1 = c1.next
            else:
                newVal = remainder
            
            hm[c] = ListNode(newVal % 10)
            remainder = int(newVal / 10) if newVal >= 10 else 0
            c += 1

        for i in range(len(hm)):
            node = hm[i]
            if i + 1 in hm:
                node.next = hm[i + 1]
            else:
                node.next = None
        
        return hm[0]

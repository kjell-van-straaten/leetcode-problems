# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''
        dummy = result = ListNode(0)
        
        while True:
            str1 = str(l1.val) + str1
            
            if l1.next == None:
                break
            else:
                l1 = l1.next
              
        while True:
            str2 = str(l2.val) + str2
            
            if l2.next == None:
                break
            else:
                l2 = l2.next
            
        outcome = str(int(str1) + int(str2))
        
        for i in range(len(outcome)):
            result.next = ListNode(int(outcome[len(outcome)-i-1]))
            result = result.next
        
        return dummy.next
        
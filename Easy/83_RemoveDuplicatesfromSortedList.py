class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):        
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else : 
                curr = curr.next

        return head


# lList = ListNode()
# lList.addNode(1)
# lList.addNode(1)
# lList.addNode(2)
lList = None
sol = Solution()
print(sol.deleteDuplicates(lList))

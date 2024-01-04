# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

      # Find lenght linked list

      curr = head
      length = 0
      while curr:
        length += 1
        curr.next
      print(length)
      
      # Do not do anything 
      if k == length: 
        return head

      if k > len(head):
        head[:] = self.rotateRight(head,len(head))
        return self.rotateRight(head,k - len(head))

        pass

      # Rotate to right when k < len(head)

      head.reverse() # In place
      head[:k] = reversed(head[:k]) # O(k)
      head[k:] = reversed(head[k:]) # O(k)
      return head
    

res = Solution()
print(res.rotateRight([0,1,2], 4))




     

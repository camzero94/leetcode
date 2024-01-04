
from typing import List
class Solution(object):
    def rotate(self, nums: List[int], k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # Solution 1
        # first = nums[k+1:]
        # second = nums[:k+1]
        # first.extend(second)
        # return first

        # Solution 2
        # Case input array is zero --> Return []
        if not len(nums):
            return []

        # Case k == 0 --> Return original array
        if not k:
            return nums

        if k > len(nums):
            # nums[:] in place  vs nums = ... create a new reference to the returned array
            nums[:] = Solution.rotate(self, nums, len(nums)) # Rotate length of array
            nums[:] = Solution.rotate(self, nums, k - len(nums))  # Rotate k - length 

        # Reverse entire array
        nums.reverse()
        # Reverse until first k
        nums[:k] = reversed(nums[:k])
        # Reverse from first k
        nums[k:] = reversed(nums[k:])
        return nums

res = Solution() 
print(res.rotate([1,2,3],4))

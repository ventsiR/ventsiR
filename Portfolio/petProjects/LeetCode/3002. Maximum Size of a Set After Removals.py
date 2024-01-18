#https://leetcode.com/problems/maximum-size-of-a-set-after-removals/description/

from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        numsInBoth = []
        numsIn1 = list(set(nums1))
        numsIn2 = list(set(nums2))
        if len(numsIn1) > len(numsIn2):
            numsIn1, numsIn2 = numsIn2, numsIn1
        numsIn2.sort()
        numsIn1Static = list(numsIn1)
        for num in numsIn1Static:            
            low = 0
            high = len(numsIn2) - 1
            while low <= high:
                mid = low + (high - low)//2
                if num == numsIn2[mid]:
                    numsIn1.remove(num)
                    numsIn2.remove(num)
                    numsInBoth.append(num)
                    break
                elif num > numsIn2[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return min(
            min(
                len(nums1)//2, 
                len(numsIn1)
            ) + min(
                len(nums2)//2, 
                len(numsIn2)
            ) + len(numsInBoth),
            (len(nums1) + len(nums2))//2)
    
solutionInstance = Solution()

print(solutionInstance.maximumSetSize([1,1,2,2,3,3], [4,4,5,5,6,6]))
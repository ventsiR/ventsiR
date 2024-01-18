#https://leetcode.com/problems/merge-sorted-array/description/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_nonzero = nums1[:m]
        lPointer = 0
        rPointer = 0
        while lPointer < m and rPointer < n:
            lVal = nums1_nonzero[lPointer]
            rVal = nums2[rPointer]
            if lVal < rVal:
                nums1[lPointer+rPointer] = lVal
                lPointer += 1
            else:
                nums1[lPointer+rPointer] = rVal
                rPointer += 1
        if rPointer >= n:
            lPointer, rPointer = rPointer, lPointer
            nums1_nonzero, nums2 = nums2, nums1_nonzero
        nums2 = nums2[rPointer:]
        index = lPointer + rPointer
        for num in nums2:
            nums1[index] = num
            index += 1
        return nums1

solutionInstance = Solution()

print(solutionInstance.merge([0], 0, [1], 1))
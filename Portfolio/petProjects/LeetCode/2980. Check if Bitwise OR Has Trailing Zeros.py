#https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/

from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        counter = 0
        for num in nums:
            if num%2 == 0:
                counter += 1
                if counter == 2:
                    return True
        return False
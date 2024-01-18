#https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagSquared = 0
        maxArea = 0
        for rectangle in dimensions:
            diagSquared = rectangle[0]**2 + rectangle[1]**2
            if diagSquared > maxDiagSquared:
                rectangleArea = rectangle[0]*rectangle[1]
                maxDiagSquared = diagSquared
                maxArea = rectangleArea
            elif diagSquared == maxDiagSquared:
                rectangleArea = rectangle[0]*rectangle[1]
                if rectangleArea > maxArea:
                    maxArea = rectangleArea
        return maxArea
    
solutionInstance = Solution()

print(solutionInstance.areaOfMaxDiagonal([3,4],[4,3]))
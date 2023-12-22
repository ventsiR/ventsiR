#---Problem: https://leetcode.com/problems/interval-list-intersections/

from typing import List

class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
        ) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(firstList):
            j = 0
            while j < len(secondList):
                firstIntvl, secondIntvl = firstList[i], secondList[j]
                if firstIntvl[0] > secondIntvl[1]:
                    secondList.remove(secondIntvl)
                elif secondIntvl[0] > firstIntvl[1]:
                    break
                else:
                    ans.append([
                        max(firstIntvl[0], secondIntvl[0] ), 
                        min(firstIntvl[1], secondIntvl[1])]
                    )
                    j += 1
            i += 1
        return ans
#https://leetcode.com/problems/minimum-moves-to-capture-the-queen/description/

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            if a == c and d in range(min(b,f), max(b,f)):
                return 2
            return 1
        if b == f:
            if b == d and c in range(min(a,e), max(a,e)):
                return 2
            return 1
        bDiag1 = c-d
        qDiag1 = e-f
        if bDiag1 == qDiag1:
            rDiag1 = a-b
            if bDiag1 == rDiag1 and a in range(min(c, e), max(c, e)):
                return 2
            return 1
        bDiag2 = c+d
        qDiag2 = e+f
        if bDiag2 == qDiag2:
            rDiag2 = a+b
            if bDiag2 == rDiag2 and a in range(min(c, e), max(c, e)):
                return 2
            return 1
        return 2
    
solutionInstance = Solution()

print(solutionInstance.minMovesToCaptureTheQueen(5, 3, 3, 4, 5, 2))
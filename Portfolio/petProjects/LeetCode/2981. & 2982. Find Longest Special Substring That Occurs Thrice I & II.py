#https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/
#https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/description/

class Solution:
    def maximumLength(self, s: str) -> int:
        freqDict = {}
        left = 0
        right = 0
        while right < len(s):
            if s[left] != s[right]:
                left = right
                if s[left] not in freqDict:
                    freqDict[s[left]] = 1
                elif freqDict[s[left]] < 3:
                    freqDict[s[left]] += 1
            else:
                while right + 3 < len(s) and s[right] == s[right + 1] == s[right + 2] == s[right + 3]:
                    right += 1
                substrlen = right-left + 1
                substr = s[left]*(substrlen)
                if substr not in freqDict:
                    freqDict[substr] = 1
                else:
                    freqDict[substr] += 1
                if substrlen > 1:
                    substr = (s[left])*(substrlen - 1)
                    if substr not in freqDict:
                        freqDict[substr] = 1
                    else:
                        freqDict[substr] += 1
                if substrlen > 2:
                    substr = (s[left])*(substrlen - 2)
                    if substr not in freqDict:
                        freqDict[substr] = 1
                    else:
                        freqDict[substr] += 1
            right += 1
        ans = -1
        for key, value in freqDict.items():
            keylen = len(key)
            if value >= 3 and keylen > ans:
                ans = len(key)
        return ans
        
# solutionInstance = Solution()

# print(solutionInstance.maximumLength('abcaba'))
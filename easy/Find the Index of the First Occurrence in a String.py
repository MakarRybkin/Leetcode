class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while i<=len(haystack):
            for j in range(len(needle)):
                if i+j>= len(haystack):
                    return -1
                if haystack[i+j]==needle[j]:
                    if j==len(needle)-1:
                        return i + j - len(needle) + 1
                else:
                    break
            i += 1

print(Solution().strStr("leetcode", "leeto"))
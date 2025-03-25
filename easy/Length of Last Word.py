class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.strip():
            return len(s.split()[-1])
        else:
            return 0
print(Solution().lengthOfLastWord(" "))
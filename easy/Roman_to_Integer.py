class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if s:
            counter = dict[s[-1]]
            for i in range(len(s)-1,0,-1):
                if dict[s[i-1]] >= dict[s[i]]:
                    counter+=dict[s[i-1]]
                else:
                    counter-=dict[s[i-1]]
            return counter
        else:
            return 0
print(Solution().romanToInt(""))
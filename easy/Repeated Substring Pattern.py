class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dividers=[1]
        if len(s)==1:
            return False
        for i in range(2, int(len(s)**0.5)+1):
            if len(s) % i == 0:
                dividers.append(i)
                if len(s)//i not in dividers:
                    dividers.append(len(s)//i)
        for i in range(len(dividers)):
            subs=s[:dividers[i]]
            if s==subs*(len(s)//dividers[i]):
                return True
        return False

print(Solution().repeatedSubstringPattern("aaaaaa"))

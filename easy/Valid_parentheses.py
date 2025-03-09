class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'(' :0, '{' :1 ,'[':2}
        dict2 = {')' :0, '}' :1 ,']':2}
        stack = []
        for i in s:
            if i in dict1:
                stack.append(i)
            else:
                if stack:
                    a=stack.pop()
                    if dict2[i]!=dict1[a]:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False

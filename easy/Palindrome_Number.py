class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            start = x
            reversed =0
            reversed += x % 10
            x //= 10
            while x>0:
                reversed *=10
                reversed += x % 10
                x //= 10
            return reversed==start
print(Solution().isPalindrome(121))



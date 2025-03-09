from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(strs, key=len)
        if min_len == 0:
            return ""
        prefix_counter = 0
        for i in range(len(min_len)):
            counter = 0
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    counter+=1
                else:
                    return strs[0][:prefix_counter]
            if counter == len(strs)-1:
                prefix_counter+=1
        return strs[0][:prefix_counter]
print(Solution().longestCommonPrefix(["a", "ab", "ab"]))




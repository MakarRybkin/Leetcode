from collections import deque
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum =[]
        pref_sum = 1
        candles=[]
        for i in range(len(s)):
            if s[i] == '*':
                prefix_sum.append(pref_sum)
                pref_sum+=1
            if s[i] == '|':
                prefix_sum.append(pref_sum)
                candles.append(i)
        result=[]
        for i in range(len(queries)):
            query = queries[i]
            l,r = 0, len(candles)-1
            start, end = query[0], query[1]
            left_candle =0
            while l<=r:
                mid = (l+r)//2
                if candles[mid]<start:
                    l = mid+1
                elif candles[mid]>=start:
                    r = mid-1
                    left_candle = candles[mid]


            l, r = 0, len(candles) - 1
            right_candle =0
            while l<=r:
                mid = (l+r)//2
                if candles[mid]<=end:
                    l = mid+1
                    right_candle = candles[mid]
                elif candles[mid]>end:
                    r = mid-1
            if left_candle >= right_candle or start == end:
                result.append(0)
            else:
                result.append(prefix_sum[right_candle]-prefix_sum[left_candle])


        return result


print(Solution().platesBetweenCandles("*|*",[[2,2]]))
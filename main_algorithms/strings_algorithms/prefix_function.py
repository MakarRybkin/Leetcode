"""
Префикс функция
Пример
a b a b a c a
[0,0,1,2,3,0,1]

Для строки s массив pi[i] — это длина наибольшего собственного префикса,
 который одновременно является суффиксом подстроки s[0..i]
"""

def prefix_function(s: str):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def find_pattern(pattern: str, text: str):
    s = pattern + "#" + text
    pi = prefix_function(s)
    m = len(pattern)
    res = []
    for i in range(len(s)):
        if pi[i] == m:
            res.append(i - 2*m)
    return res


print(find_pattern("aba", "abacaba"))  # [0, 4]
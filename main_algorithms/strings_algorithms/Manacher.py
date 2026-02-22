"""
Алгоритм Манакера (англ. Manacher's algorithm) — алгоритм с линейным временем работы, позволяющий
получить в сжатом виде информацию обо всех палиндромных подстроках заданной строки.

Он позволяет найти все палиндромы за O(n).

Дана строка s.
Нужно для каждой позиции узнать:

длину максимального палиндрома с центром здесь

или найти самый длинный палиндром в строке

сложность
преобразование	O(n)
основной цикл	O(n)
итог	O(n)
"""

def manacher_odd(s):
    s = '$' + s + '^'
    n = len(s)
    res = [0] * n
    l = 0
    r = 0
    for i in range(1, n - 1):
        res[i] = max(0, min(r - i, res[l + (r - i)]))
        while s[i - res[i]] == s[i + res[i]]:
            res[i] += 1
        if i + res[i] > r:
            l = i - res[i]
            r = i + res[i]
    return res[1:-1]

def manacher(s):
    res = manacher_odd('#' + '#'.join(s) + '#')[1:-1]
    return ([x // 2 for x in res[::2]], [x // 2 for x in res[1::2]])



def longest_palindrome(s: str):
    d1, d2 = manacher(s)
    n = len(s)

    best_len = 0
    best_pos = 0

    # нечётные
    for i in range(n - 1):
        length = 2 * d1[i] - 1
        if length > best_len:
            best_len = length
            best_pos = i - d1[i] + 1

    # чётные
    for i in range(n - 1):
        length = 2 * d2[i]
        if length > best_len:
            best_len = length
            best_pos = i - d2[i]

    return s[best_pos:best_pos + best_len]

print(longest_palindrome("abbaabacaba"))  # abacaba
print(manacher("abbaabacaba")) # ([1, 1, 1, 1, 1, 2, 1, 4, 1, 2, 1], [0, 2, 0, 2, 0, 0, 0, 0, 0, 0])

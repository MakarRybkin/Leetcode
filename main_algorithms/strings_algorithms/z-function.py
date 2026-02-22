"""
Дано:
строка text и строка pattern
Нужно найти все позиции, где pattern входит в text.
pattern + "#" + text

Вычисление Z-функции: O(n)

поиск подстроки: O(n)
"""
def z_function(s: str):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def find_pattern(pattern: str, text: str):
    s = pattern + "#" + text
    z = z_function(s)
    m = len(pattern)
    result = []
    for i in range(m + 1, len(s)):
        if z[i] == m:
            result.append(i - m - 1)  # позиция в text
    return result


text = "abacaba"
pattern = "aba"
print(find_pattern(pattern, text))  # [0, 4]
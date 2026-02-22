"""
1. Даны строки  T  и  S . Научится находить позиции всех вхождений  S  в  T .  O(|T|+|S|) .
"""

# стандартное обратное полиномиальное хеширование
m = 10 ** 9 + 7 # число, по остатку по которому мы будем все считать, чаще всего простое, но в целом необязательно
k = 31 # Число большее алафита, желательно тоже простое, ОЧЕНЬ желательно, чтобы m было взаимно просто с k
k_powers = [1]
for t in range(10000):
    k_powers.append((k_powers[-1] * k) % m)

def stringHash(S):
    global m, k, k_powers
    hash_list = [0] # будем считать, что хеш пустой строки = 0, считаем хеш на каждой подстроке
    for i in range(len(S)):
        char_num = ord(S[i]) - ord('a') + 1 # мы не хотим нулевых хешей, иначе hash(a...a) == hash(a...a) = 0
        hash_list.append((hash_list[-1] * k + char_num) % m)
    return hash_list

def stringHashSubstring(hashS, l, r): # будем жить в 0-индексации
    global m, k, k_powers
    num = 0
    return ((hashS[r + 1] - hashS[l] * k_powers[r - l + 1]) % m + m) % m

def findAllOccurencesWithHash(S, T):
    hash_S = stringHash(S)
    hash_T = stringHash(T)[-1] # для второй нам интересен только хеш на всей строке
    result = []
    for i in range(len(S) - len(T) + 1):
        if hash_T == stringHashSubstring(hash_S, i, i + len(T) - 1):
            result.append(i)
    return result

# print(stringHash("abab"))
# 33
# print(31746 - 33*31*31)
# print(31*31*1 + 31*2 +1*1)
print(findAllOccurencesWithHash('aababacabaaab', 'ab'))
print(findAllOccurencesWithHash('aababacabaaab', 'aa'))

# Вычисление хешей – O(S + T), потом просто O(S-T) проверок
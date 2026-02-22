"""
1-d prefix sum
"""
def func(x, y):
    return x + y

def PrefixArray(a):
    pf = [0]
    for t in range(len(a)):
        pf.append(func(pf[-1], a[t]))
    return pf
a = [3, 1, 4, 1, 5, 9, 2, 6]
pf = PrefixArray(a)
print(pf)

queries = [(3, 4), (1, 5), (6, 7), (6, 6)] # 1-индексация

for (l, r) in queries:
    print(pf[r] - pf[l - 1])

"""
3-d prefix sum
"""
a = [
    [[1, 2, 3],
     [3, 2, 1],
     [1, 1, 1]],

    [[1, 2, 3],
     [3, 2, 2],
     [1, 3, 3]],

    [[3, 2, 3],
     [3, 2, 1],
     [1, 1, 1]]]

def prefixSum3D(a):
    pf = []
    for i in range(len(a) + 1):
        x = []
        for j in range(len(a[0]) + 1):
            x.append((len(a[0][0]) + 1) * [0])
        pf.append(x)

    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(a[0][0])):
                pf[i + 1][j + 1][k + 1] = a[i][j][k] + pf[i + 1][j + 1][k] + pf[i + 1][j][k + 1] + pf[i][j + 1][k + 1] - pf[i + 1][j][k] - pf[i][j + 1][k] - pf[i][j][k + 1] + pf[i][j][k]

    return pf

pf = prefixSum3D(a)
for t in pf:
    print(t)

Q = [((1, 2, 1), (2, 2, 3))]
for ((xl, yl, zl), (xr, yr, zr)) in Q:
    print(pf[xr][yr][zr] - pf[xr][yr][zl - 1] - pf[xr][yl - 1][zr] - pf[xl - 1][yr][zr] + pf[xl - 1][yl - 1][zr] + pf[xl - 1][yr][zl - 1] + pf[xr][yl - 1][zl - 1] - pf[xl - 1][yl - 1][zl - 1])

    for i in range(xl - 1, xr):
        for j in range(yl - 1, yr):
            for k in range(zl - 1, zr):
                print(a[i][j][k])
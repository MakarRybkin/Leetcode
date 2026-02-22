"""
Дан набор из  n  отрезков на прямой, заданных координатами начал и концов  [li,ri] .
 Требуется найти любую точку на прямой, покрытую наибольшим количеством отрезков.
"""
lr = [
    [1, 3],
    [2, 4],
    [5, 21],
    [-94, 32],
    [3, 4],
    [54, 94]
]


# Будем считать количество открытых отрезков на данный момент

def pointWithMaxCollisions(lr):
    cur = 0
    begin_and_end = []
    for [l, r] in lr:
        begin_and_end.append((l, -1)) # хотим, чтобы начала находились раньше, чтобы мы их обработали раньше
        begin_and_end.append((r, +1)) # т.к. считаем что чел на точка находится внутри отрезка даже в конец жизни
    begin_and_end.sort()
    cur_open = 0
    best_point = begin_and_end[0][0]
    best_open = 0
    for i in range(len(begin_and_end)):
        cur_open -= begin_and_end[i][1]
        if cur_open > best_open:
            best_open = cur_open
            best_point = begin_and_end[i][0]
    return best_point

pointWithMaxCollisions(lr)

"""
Дан набор из  n  отрезков на прямой, заданных координатами начал и концов  [li,ri] .
 Требуется для каждого отрезка сказать сколько отрезков с ним пересекаются.
"""
from bisect import bisect_right, bisect_left

# какие же отрезки нам не подходят?
# Те, у кого конец раньше нашего начала
# Те, у кого начало позже нашего конца
# остальные нам подходят

def numberOfSegmentsForAllSegments(lr):
    l_sorted = []
    r_sorted = []
    for (l, r) in lr:
        l_sorted.append(l)
        r_sorted.append(r)
    l_sorted.sort()
    r_sorted.sort()
    results = {}
    for (l, r) in lr:
        results[(l, r)] = bisect_right(l_sorted, r) - 1 - bisect_left(r_sorted, l)
    return results
numberOfSegmentsForAllSegments(lr)
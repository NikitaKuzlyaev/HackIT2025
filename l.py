import math
from typing import List, Tuple
 
 
def solve(n_dots: int, dots: list[tuple[int, int]]) -> float | int:
    distances = []
    size = [1] * n_dots
    comp = [i for i in range(n_dots)]
 
    def cap(x: int) -> int:
        replace = []
        while x != comp[x]:
            replace.append(x)
            x = comp[x]
 
        for p in replace:
            comp[p] = x
        return x
 
    def unite(a: int, b: int) -> bool:
        a, b = cap(a), cap(b)
        if a == b:
            return False
 
        if size[a] < size[b]:
            a, b = b, a
 
        comp[b] = a
        size[a] += size[b]
        return True
 
    def r2distance(d1: tuple[int, int], d2: tuple[int, int]) -> int:
        dist = (d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2
        return dist
 
    for i in range(n):
        for j in range(i + 1, n):
            r2 = r2distance(dots[i], dots[j])
            distances.append((r2, i, j))
 
    distances.sort()
    #print(distances)
    n_components = n
    for r2, i, j in distances:
        if unite(i, j):
            n_components -= 1
 
            if n_components == 1:
                return math.sqrt(r2)
 
    return -1
 
 
if __name__ == '__main__':
    n = int(input())
    d = [tuple(map(int, input().split())) for i in range(n)]
 
    result = solve(n, d)
    print("%.12f" % result)

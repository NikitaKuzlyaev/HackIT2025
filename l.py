from typing import List, Tuple
import sys
 
sys.setrecursionlimit(10 ** 5)
 
 
def solve(n_dots: int, dots: list[tuple[int, int]]) -> float | int:
    def dis(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
 
    def check(h):
        visited = [False] * len(dots)
        dfs(0, h, visited)
        return all(visited)
 
    def dfs(v, h, visited):
        visited[v] = True
        for u in range(len(dots)):
            if not visited[u] and dis(dots[v], dots[u]) <= h:
                dfs(u, h, visited)
 
    diameter = 2 * (2 * 10 ** 9)
    l, r = 0, diameter
 
    while r - l > 10 ** (-7):
        mid = (l + r) / 2
        if check(mid):
            r = mid
        else:
            l = mid
 
    return l
 
 
if __name__ == "__main__":
    n = int(input())
    d = [tuple(map(int, input().split())) for i in range(n)]
 
    result = solve(n, d)
    print("%.7f" % result)

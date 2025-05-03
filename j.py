import sys
from math import gcd


def solve(n, a, k):
    p = {}

    for i in range(1, min(k + 1, int(k ** 0.5 + 4))):
        if k % i == 0:
            p[i] = 0
            p[k // i] = 0

    for i in range(len(a)):
        for d in p:
            if a[i] % d == 0:
                p[d] += 1

    res = 0
    for i in range(len(a)):
        if a[i] % k == 0:
            res += len(a) - 1
        else:
            g = gcd(a[i], k)
            res += p[k // g] - (a[i] % (k // g) == 0)

    res = res // 2
    res = res / (n * (n - 1) // 2)

    print('%.15f' % res)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())

    solve(n, a, k)

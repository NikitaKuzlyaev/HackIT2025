
import sys


def solve(n, m, d, l):
    if m < n:
        print('NO')
        return

    l.sort(reverse=True)
    res = 0
    right = m - 1
    for left in range(m):
        if left > right:
            break

        if l[left] >= d:
            res += 1
        else:
            while right > left:
                if l[right] + l[left] - 1 >= d:
                    res += 1
                    right -= 1
                    break
                else:
                    right -= 1

    if res >= n:
        print('YES')
    else:
        print('NO')
    return


if __name__ == '__main__':
    n, m, d = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    solve(n, m, d, l)

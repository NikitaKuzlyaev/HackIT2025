import sys

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

su = sum(c)
mx = max(c)

su = su - mx

if mx > su + 2:
    print('NO')
else:
    print('YES')

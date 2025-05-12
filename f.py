
import sys
 
 
def solve():
    k, n = map(int, sys.stdin.readline().split())
    s = str(sys.stdin.readline().strip())
 
    res = k
 
    dp = [[0 for i in range(k + 1)] for j in range(k + 1)]
    for length in range(2, k + 1):
        for start in range(0, k - length + 1):
            end = start + length - 1
 
            dp[start][end] = dp[start + 1][end - 1] + int(s[start] != s[end])
 
            if dp[start][end] <= n:
                res += 1
 
    sys.stdout.write(str(res) + '\n')
 
 
if __name__ == '__main__':
    solve()

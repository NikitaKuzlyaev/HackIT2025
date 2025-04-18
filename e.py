def solve():
    n = int(input())
 
    if 2 <= n <= 3:
        print(-1)
        return
 
 
    f = [[0] * (2 * i + 1) for i in range(n)]
 
    cur_yellow = 1
    cur_white = 1 + (1 + (n - 1)) * (n - 1) // 2
 
    for i in range(n - 1):
        for j in range(2 * i + 1):
            if (i + j) % 2 == i % 2:
                f[i][j] = cur_yellow
                cur_yellow += 1
            else:
                f[i][j] = cur_white
                cur_white += 1
 
    cur_yellow = n ** 2 - n + 1
    cur_white = cur_yellow - n + 1
    for j in range((n - 1) * 2 + 1):
        if j % 2 == 0:
            f[n - 1][j] = cur_yellow
            cur_yellow += 1
        else:
            f[n - 1][j] = cur_white
            cur_white += 1
 
    for i in f:
        print(*i)
 
 
solve()

def solve():
    n, m = map(int, input().split())
 
    f = [['#'] * (m + 2)]
 
    for _ in range(n):
        row = list(input().strip())
        f.append(['#'] + row + ['#'])
 
    f.append(['#'] * (m + 2))
 
    v = [lambda x, y: (x + 1, y),
         lambda x, y: (x - 1, y),
         lambda x, y: (x, y + 1),
         lambda x, y: (x, y - 1),
         ]
 
    q = []
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if f[x][y] == 'x':
                q.append((x, y))
 
    res = []
    cur = 0
    new_q = []
    for day in range(1, n + m - 1):
        while len(q) > 0:
            x, y = q.pop()
 
            for d in v:
                nx, ny = d(x, y)
                if f[nx][ny] == 'o':
                    f[nx][ny] = '#'
                    cur += 1
                elif f[nx][ny] == '.':
                    f[nx][ny] = 'x'
                    new_q.append((nx, ny))
 
        res.append(cur)
        q, new_q = new_q, []
 
    print(*res)
 
 
solve()

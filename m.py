n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

uniq = set(a)
uniq = list(uniq)
uniq.sort()

INF = 1 << 120

dp = [c[0] * abs(a[0] - i) for i in uniq]
new_dp = [INF for i in range(len(uniq))]

for i in range(1, n):
    mn_prev = INF
    for j in range(len(uniq)):
        mn_prev = min(mn_prev, dp[j])

        new_dp[j] = (mn_prev + c[i] * abs(a[i] - uniq[j]))

    dp, new_dp = new_dp, dp

res = min(dp)
if res == INF:
    print(-1)
else:
    if res > 10**16: # such validation i think <3
        1/0
    else:
        print(res)

import sys
import random

n = int(input())

res = [100]
stack = [(100, 0)]
ans_on_pref = [0]
prev_v = 0

for i in range(n - 2):
    print(f"? {0} {i + 1}")
    sys.stdout.flush()

    v = int(input())
    x = 0

    if prev_v + stack[-1][0] >= v:
        x = v - prev_v
        prev_v = v
    else:
        while len(stack) > 0:
            h, idx = stack.pop()

            vr = v - ans_on_pref[idx]
            if vr % (i + 1 - idx) != 0:
                continue

            x = vr // (i + 1 - idx)
            if x > h:
                x = 0
                continue

            stack.append((h, idx))
            break

    res.append(x)
    ans_on_pref.append(v)
    stack.append((x, i + 1))

res.append(100)
print("!", end=" ")
print(*res)
sys.stdout.flush()


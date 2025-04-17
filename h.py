t = int(input())

for _ in range(t):
    s = str(input())

    res = ""
    for idx, ch in enumerate(s, start=1):
        res += "abcde"[(idx + ord(ch) - ord('a')) % 5]

    print(res)

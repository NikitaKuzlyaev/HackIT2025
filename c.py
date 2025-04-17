
# c.py

def solve():
    vitek = 'VITEK'

    teams = {i: 0 for i in vitek}

    for i in range(5):
        teams[vitek[i]] = sum(map(int, input().split()))

    res = ''

    for i in vitek:
        cur = teams[i]
        other = [teams[j] for j in vitek if j != i]
        other.sort(reverse=True)

        for idx, el in enumerate(other, start=1):
            if idx + el > cur + 5:
                break
        else:
            res += i

    if res == vitek:
        res += '!'

    print(res)
    return


if __name__ == '__main__':
    solve()

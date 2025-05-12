def solve(notes):
    if len(notes) > 26:
        return 1
    return 1 if len(set(notes)) < len(notes) else len(notes)
 
 
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        res = solve(input())
        print(res)

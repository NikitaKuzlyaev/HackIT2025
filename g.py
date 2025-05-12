MOD = 10 ** 9 + 7
MAX_NM = 100
 
factorials = [1] * (MAX_NM + 1)
for i in range(1, MAX_NM + 1):
    factorials[i] = (factorials[i - 1] * i) % MOD
 
 
def solve(n: int, m: int) -> int:
    def modular_division(a: int, b: int, mod: int) -> int:
        inv_b = pow(b, mod - 2, mod)
        return (a * inv_b) % mod
 
    total = 0
    for groups_of_2_possible in range(n // 2, -1, -1):
        remaining_students = n - groups_of_2_possible * 2
        n_teams_with_3 = remaining_students
        n_teams_with_2 = groups_of_2_possible - n_teams_with_3
 
        if n_teams_with_2 < 0:
            break
 
        total_groups = n_teams_with_2 + n_teams_with_3
 
        if total_groups > m:
            continue
 
        student_permutations = factorials[n]
 
        for _ in range(n_teams_with_2):
            student_permutations = modular_division(student_permutations, factorials[2], MOD)
 
        for _ in range(n_teams_with_3):
            student_permutations = modular_division(student_permutations, factorials[3], MOD)
 
        student_permutations = modular_division(student_permutations, factorials[n_teams_with_3], MOD)
        student_permutations = modular_division(student_permutations, factorials[n_teams_with_2], MOD)
 
        lab_permutations = factorials[m]
        unused_labs = m - total_groups
        lab_selections = modular_division(lab_permutations, factorials[unused_labs], MOD)
 
        total = (total + lab_selections * student_permutations) % MOD
 
    return total
 
 
if __name__ == '__main__':
    n, m = map(int, input().split())
 
    print(solve(n, m))

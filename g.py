
import random
import itertools

MOD = 10 ** 9 + 7
MAX_NM = 100

FACTS = [1] * (MAX_NM + 1)
for i in range(1, MAX_NM + 1):
    FACTS[i] = (FACTS[i - 1] * i) % MOD


def divide_by_modulo(a: int, b: int, m: int) -> int:
    """Делим a на b по простому модулю m"""
    b_ = pow(b, m - 2, m)  # Умножение на b_ по модулю равнозначно делению на b
    res = (a * b_) % m
    return res


def stupid(n: int, m: int) -> int:
    """
    Точно верное решение с полным перебором для проверки основного решения на небольших входных данных
    """
    pn = itertools.permutations(list(range(n)))
    uniq = set()  # Сохраняем пары ((команды: tuple[tuple, ...]), (работы: tuple[int, ...]))
    for ppn in pn:
        for n_teams_prev in range(n // 2, -1, -1):
            n_teams_with_3 = n - n_teams_prev * 2
            n_teams_with_2 = n_teams_prev - n_teams_with_3
            if n_teams_with_2 < 0:
                break
            n_teams = n_teams_with_2 + n_teams_with_3
            if n_teams > m:
                continue
            pm = itertools.combinations(list(range(m)), n_teams)
            cur_teams = []
            it = 0
            for _ in range(n_teams_with_3):
                new_team = []
                for i in range(3):
                    new_team.append(ppn[it])
                    it += 1
                new_team.sort()
                cur_teams.append(tuple(new_team))
            for _ in range(n_teams_with_2):
                new_team = []
                for i in range(2):
                    new_team.append(ppn[it])
                    it += 1
                new_team.sort()
                cur_teams.append(tuple(new_team))
            cur_teams.sort()
            cur_teams = tuple(cur_teams)
            for ppm in pm:
                for pppm in itertools.permutations(ppm):
                    uniq.add((cur_teams, pppm))

    # print(f)
    # for i in sorted(list(uniq)):
    #     print(i)
    # print(uniq)
    return len(uniq)


def solve(n: int, m: int) -> int:
    """
    main solution. Основное решение
    """
    total = 0  # Общее число вариантов по всем разбиениям. Тут накапливается ответ.

    for n_teams_prev in range(n // 2, -1, -1):
        """
        Перебираю число <первичных команд>.
        Условно выстраиваю студентов в ряд, объединяю в команду по 2 человека первые [n_teams_prev пар]
        Остается [n - n_teams_prev * 2] студентов.
        Так как команды по 2 или по 3, то докидываю оставшихся студентов в первые с начала ряда команды по 2 человека.
        """
        n_teams_with_3 = n - n_teams_prev * 2  # Столько команд по 3 человека. Это как раз те <остатки>
        n_teams_with_2 = n_teams_prev - n_teams_with_3  # Остальные команды по 2 человека

        if n_teams_with_2 < 0:  # Если команды по 2 ушли в минус, что не может быть в задаче, то завершаем работу (т.к. дальше только меньше будет)
            break

        n_teams = n_teams_with_2 + n_teams_with_3  # Итого у нас столько команд

        if n_teams > m:  # Для избежания ошибки деления на 0 по модулю, сразу пропускаем итерацию, если лабораторных не хватит на все команды
            continue  # Равносильно прибавлению нуля вариантов к ответу при текущем разбиении

        n_student_permutations = FACTS[n]  # Сколько у нас есть вариантов выстроить студентов в ряд. Просто факториал
        n_groups = n_student_permutations  # Сохраним его еще тут. Для промежуточных вычислений

        for _ in range(n_teams_with_2):
            """
            Делим на 2! столько раз, сколько команд по 2 человека.
            Пример:
            [1 3 5] [4 2] - здесь 4 и 2 в одной команде, но [1 3 5] [2 4] это тоже самое
            """
            n_groups = divide_by_modulo(n_groups, FACTS[2], MOD)

        for _ in range(n_teams_with_3):
            """
            Делим на 3! столько раз, сколько команд по 3 человека.
            Пример:
            [1 3 5] [4 2] - здесь 1, 3 и 5 в одной команде, но [1 5 3] [4 2] или [3 5 1] [4 2] и т.п. - это тоже самое
            """
            n_groups = divide_by_modulo(n_groups, FACTS[3], MOD)

        n_groups = divide_by_modulo(n_groups, FACTS[n_teams_with_3], MOD)
        n_groups = divide_by_modulo(n_groups, FACTS[n_teams_with_2], MOD)

        n_labs_permutations = FACTS[m]  # Сколько есть вариантов расположить лабораторные в ряд. Это просто факториал [m]
        n_unused_labs = m - n_teams  # Условимся распределить между мини-группами только первые [n_teams] работ. Тогда есть остаток
        n_first_labs = divide_by_modulo(n_labs_permutations, FACTS[n_unused_labs], MOD)  # Сколько есть упорядоченных вариантов выбора [n_teams] работ из [m]

        variants = n_first_labs * n_groups

        total = (total + variants) % MOD  # Обновляем ответ (прибавляем число найденных разбиений в текущей конфигурации размеров команд)

    total = total % MOD  # Подстраховка
    return total


def auto_tester(max_n: int, max_m: int, n_tests: int, ground_truth: callable, solution: callable) -> bool:
    """
    Проверка решения solution. Предполагаем, что решение ground_truth истинно верное
    """
    for test in range(n_tests):
        n = random.randint(3, max_n)
        m = random.randint(1, max_m)

        true_res = ground_truth(n, m)
        res = solution(n, m)
        print(f"n={n} m={m} true={true_res} solution={res}")
        if true_res != res:
            # pass
            return False

    return True


if __name__ == '__main__':
    DEBUG = False

    if DEBUG:
        v = auto_tester(7, 7, 1000, stupid, solve)
        if v:
            print('Ok ^-^')
        else:
            print('Solution is wrong!')
    else:
        n, m = map(int, input().split())
        result = solve(n, m)
        print(result)

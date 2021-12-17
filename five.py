'''E. Версия 0.9.9.9.9.9....'''

MODULES = [int(i) for i in input().split()]
RULES = [list(map(int, input().split())) for _ in range(int(input()))]
RULES_DICT = {1: 1, 2: 1, 3: 1}


def main():
    prod = list(product(range(1, MODULES[0] + 1), range(1, MODULES[1] + 1), range(1, MODULES[2] + 1)))

    res = len(prod)
    for ver in prod:
        valid = True
        for rule in RULES:
            xi, xver, yi, yver = rule
            if ver[xi - 1] >= xver and ver[yi - 1] < yver:
                valid = False
                break
        if not valid:
            res -= 1
    print(res)


def product(*args):
    result = [[]]
    for pool in map(tuple, args):
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


if __name__ == '__main__':
    main()



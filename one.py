'''A. Медиана с вычитанием'''

MASSIVE = [int(i) for i in input().split()]
MASSIVE_SORTED = sorted(MASSIVE)


def operation(args):
    mas = args[0]
    mas[args[1]] = MASSIVE[args[1]] - MASSIVE[args[2]]
    return mas


def is_median(index):
    if MASSIVE[index] == MASSIVE_SORTED[1]:
        return True
    for tmp_massive in map(operation, ((MASSIVE.copy(), i, j) for i in range(3) for j in range(3) if i != j)):
        if tmp_massive.index(sorted(tmp_massive)[1]) == index:
            return True
    return False


def main():
    for elem in map(is_median, range(3)):
        print("YES" if elem else "NO")


if __name__ == '__main__':
    main()

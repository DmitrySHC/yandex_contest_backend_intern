'''B. Яндекс.Бар'''


N, M = (int(i) for i in input().split())
GLASS = [input() for _ in range(N)]
INGREDIENTS = [input().split()[1:] for i in range(int(input()))]


def feel(ing):
    global N
    for i in range(N - 2, N - 2 - int(ing[0]), -1):
        GLASS[i] = GLASS[i].replace(" ", ing[1])
    N -= int(ing[0])


def main():
    for elm in INGREDIENTS:
        feel(elm)
    print(*GLASS, sep='\n')


if __name__ == '__main__':
    main()

'''C. Защитники башни'''

N, M = (int(i) for i in input().split())
BLOCKS = [int(i) for i in input().split()]
GUARDIANS = sorted([int(i) for i in input().split()])
BLOCKS.reverse()


def count_areas():
    max_block = BLOCKS[0]
    sun_areas = [BLOCKS[0]]
    for block in BLOCKS:
        if block - max_block > 0:
            sun_areas += [block - max_block]
            max_block = block
    return sorted(sun_areas)


def main():
    sun_areas = count_areas()
    index_guard = index_sun = 0
    count = 0
    for _ in range(len(GUARDIANS) + len(sun_areas)):
        if index_sun < len(sun_areas) and sun_areas[index_sun] >= GUARDIANS[index_guard]:
            count += 1
            index_guard += 1
        index_sun += 1
    print(count)


if __name__ == '__main__':
    main()

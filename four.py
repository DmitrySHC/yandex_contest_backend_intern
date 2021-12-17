'''D. Считаем клетки'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.edge = False
        # self.in_edge = False
        self.out_of_edge = True

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # def __gt__(self, other):
    #     return self.x > other.x or self.y > other.y
    #
    # def __ge__(self, other):
    #     return self.x >= other.x and self.y >= other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'X' if self.edge else f'.'


N, M = (int(i) for i in input().split())

# MATRIX = [['.'] * N for i in range(M)]

MATRIX = []
for x in range(N + 2):
    MATRIX.append([''] * (M+2))
    for y in range(M+2):
        MATRIX[x][y] = Point(x=x, y=y)


CORNERS = []
for _ in range(int(input())):
    tmp = input().split()
    CORNERS += [Point(int(tmp[0]), int(tmp[1]))]
CORNERS.append(CORNERS[0])

DIRECTIONS = {
    'stop': Point(0, 0),
    'right': Point(1, 0),
    'left': Point(-1, 0),
    'up': Point(0, 1),
    'down': Point(0, -1),
    'right_up': Point(1, 1),
    'left_up': Point(-1, 1),
    'left_down': Point(-1, -1),
    'right_down': Point(1, -1),
}

EDGE = []


def elem_move(from_point, to_point, direction_key):
    direction = DIRECTIONS[direction_key]
    while True:
        MATRIX[from_point.y][from_point.x].edge = True
        EDGE.append(MATRIX[from_point.y][from_point.x])
        from_point += direction
        if from_point == to_point:
            break


def construct():
    prev_point = CORNERS[0]
    for corner in CORNERS:
        start = prev_point
        end = corner
        dif = end - start
        direction = 'stop'
        if dif.x == 0 and dif.y > 0:
            direction = 'up'
        elif dif.x == 0 and dif.y < 0:
            direction = 'down'
        elif dif.x < 0 and dif.y == 0:
            direction = 'left'
        elif dif.x > 0 and dif.y == 0:
            direction = 'right'
        elem_move(start, end, direction_key=direction)
        prev_point = end
        # ========================
        print()
        for elem in MATRIX:
            print(' '.join(map(str, elem)))
        # ========================


construct()
print(f'edge: {len(EDGE) - 1}')

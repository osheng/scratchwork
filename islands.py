from typing import List, Union, Tuple
from random import seed, randint

seed(1)
"""

"""


def random_arr(n: int) -> List[List[Union[int, int]]]:
    return [[randint(0, 1) for _ in range(n)] for _ in range(n)]


def print_map(nxn: List[List[Union[int, int]]]) -> None:
    for row in nxn:
        print(row)


def list_vertices(nxn: List[List[Union[int, int]]]) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(len(nxn)) for c in range(len(nxn[0])) if nxn[r][c] == 1]


def is_neighbor(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) < 2


def count_components(vertices: List[Tuple[int, int]]) -> int:
    total = 0
    q = []  # current island is empty
    while len(vertices) > 0:  # empty vertices island by island
        if len(q) == 0:
            q.append(vertices.pop(0))
            total += 1
        while len(q) > 0:
            current = q.pop(0)
            for v in vertices:
                if is_neighbor(v, current):
                    q.append(v)
                    vertices.remove(v)

    return total


def count_islands(nxn: List[List[Union[int, int]]]) -> int:
    vertices = list_vertices(nxn)
    return count_components(vertices)


if __name__ == '__main__':
    nxn = random_arr(4)
    print_map(nxn)

    print(count_islands(nxn))

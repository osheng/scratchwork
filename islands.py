from typing import List, Union, Tuple
from random import seed, randint

seed(1)
"""

"""


def random_arr(n: int) -> List[List[Union[int, int]]]:
    return [[randint(0, 1) for _ in range(n)] for _ in range(n)]


def print_map(island_map: List[List[Union[int, int]]]) -> None:
    for row in island_map:
        print(row)


def list_vertices(island_map: List[List[Union[int, int]]]) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(len(island_map)) for c in range(len(island_map[0])) if island_map[r][c] == 1]


def is_neighbor(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) < 2


def get_neighbors(v: Tuple[int, int], vertices: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    possible_neighbors = [(v[0] - 1, v[1]), (v[0] + 1, v[1]), (v[0], v[1] - 1), (v[0], v[1] + 1)]
    # TODO the keyword in linear searches, to avoid this need something else
    return [p for p in possible_neighbors if p in vertices]


def count_components(vertices: List[Tuple[int, int]]) -> int:
    total = 0
    q = []  # current island is empty
    while len(vertices) > 0:  # empty vertices island by island
        if len(q) == 0:
            q.append(vertices.pop(0))
            total += 1
        while len(q) > 0:
            current = q.pop(0)

            # TODO: rather than going through all neighbours, I should binary search for all possible neighbours
            neighbors = get_neighbors(current, vertices)
            for neighbor in neighbors:
                q.append(neighbor)
                # TODO: runtime of remove could likely be improved
                vertices.remove(neighbor)

            # Here's a suboptimal way of doing things
            # i = 0
            # while i < len(vertices):
            #     if is_neighbor(vertices[i], current):
            #         q.append(vertices[i])
            #         vertices.remove(vertices[i])
            #     else:
            #         i += 1

    return total


def count_islands(island_map: List[List[Union[int, int]]]) -> int:
    vertices = list_vertices(island_map)
    return count_components(vertices)


if __name__ == '__main__':
    nxn = random_arr(5)
    print_map(nxn)
    print(count_islands(nxn))
    seed(1)
    print(f"count_islands(4x4) returns {count_islands(random_arr(4))} and it should return 3")
    seed(1)
    print(f"count_islands(5x5) returns {count_islands(random_arr(5))} and it should return 3")
    seed(1)
    print(f"count_islands(6x6) returns {count_islands(random_arr(6))} and it should return 6")

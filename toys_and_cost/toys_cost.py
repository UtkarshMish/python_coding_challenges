
from typing import List


def difference(a: int, b: int, *args) -> int:
    return max(a, b, *args) - min(a, b, *args)


def get_iter(a: int, b: int) -> int:
    return 1 if a >= 0 and b >= 0 and min(a, b) == a else -1


def calc_max_toys(no_of_shops: int,
                  shops: int,
                  position: int,
                  moves_allowed: int,
                  distances: List[int],
                  toys: List[int]) -> int:
    total_toys_collected: int = 0
    collected_list: List[int] = list()
    if position in distances:
        total_toys_collected += toys[distances.index(position)]
        toys.pop(distances.index(position))
        distances.pop(distances.index(position))

    if len(distances) != shops:
        distances = distances[:shops]
    list_of_items = sorted([*zip(distances, toys)],
                           key=lambda value: difference(value[0], position, value[1]), reverse=True)

    for distance, toy_value in list_of_items:
        if difference(position, distance) <= moves_allowed and not(distance in collected_list):

            for dist in range(position+1, distance, get_iter(position, distance)):

                if dist in distances:
                    total_toys_collected += toys[distances.index(dist)]
                    collected_list.append(dist)

            total_toys_collected += toy_value
            moves_allowed -= difference(position, distance)
            position = distance
    return total_toys_collected


if __name__ == "__main__":
    no_of_shops = int(input())
    shops, initial_position, moves_allowed = (
        int(value) for value in input().split(' ')
    )
    distances = [int(value.strip())
                 for value in input().strip("[").strip("]").split(",")]
    toys = [int(value.strip())
            for value in input().strip("[").strip("]").split(",")]
    max_toys = calc_max_toys(
        no_of_shops, shops, initial_position, moves_allowed, distances, toys)

    print(max_toys)

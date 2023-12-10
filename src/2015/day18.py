from sympy.utilities.iterables import multiset_permutations
from typing import List

def read(path: str) -> str:
    return open(path, "r").read()

# Convert input to 2d array for proper indexing
def get_2d_arr(txt: str) -> List[List]:
    arr = [list(row) for row in txt.splitlines()]

    return arr

neighbours = list(multiset_permutations([-1, 1, -1, 0, 1], 2))
def animate_lights(lights: List[List], counter: int, part2: bool = False) -> List[List]:

    # Define next array and for part 2, the always on LEDS
    next_arr = [['.' for i in range(len(lights))] for j in range(len(lights))]
    always_on = list(multiset_permutations([0, 0, len(lights)-1, len(lights)-1], 2))

    # Iterate through each LED
    for i in range(len(lights)):
        for j in range(len(lights)):
            total_on = 0

            # Iterate through each neighbour and check state
            # Do not allow negative indices to avoid jumping past array edge
            for n in neighbours:
                row_shift = n[0]
                col_shift = n[1]

                try:
                    if lights[i + row_shift][j + col_shift] == '#' \
                        and (i + row_shift) >= 0 and (j + col_shift) >= 0:
                        total_on += 1
                except Exception:
                    pass

            # Extra logic for part 2 always on LEDs

            if part2 and ([i, j] in always_on):
                next_arr[i][j] = '#'
            else:
                if lights[i][j] == '#':
                    if total_on in [2, 3]:
                        next_arr[i][j] = '#'
                    else:
                        next_arr[i][j] = '.'
                elif lights[i][j] == '.':
                    if total_on == 3:
                        next_arr[i][j] = '#'
                    else:
                        next_arr[i][j] = '.'

    if counter == 1:
        return next_arr
    else:
        return animate_lights(next_arr, counter - 1, part2)

if __name__ == "__main__":
    inpt = read("./inputs/day18.txt")
    arr = get_2d_arr(inpt)

    # Part 1
    final_arr = animate_lights(arr, 100)
    sum_on = sum(sum(1 for n in row if n == '#') for row in final_arr)
    print(sum_on)

    # Part 2
    # Set corners to on
    arr[0][0] = '#'
    arr[0][len(arr)-1] = '#'
    arr[len(arr)-1][0] = '#'
    arr[len(arr)-1][len(arr)-1] = '#'

    final_arr2 = animate_lights(arr, 100, True)
    sum_on2 = sum(sum(1 for n in row if n == '#') for row in final_arr2)
    print(sum_on2)




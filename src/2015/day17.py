from typing import List, Tuple
from itertools import combinations

def read(path:str) -> str:
    o = open(path, "r").read()

    arr = []
    for n in o.splitlines():
        arr.append(int(n))

    return arr

def get_combinations(i: List) -> Tuple[int, int]:

    # Using itertools.combinations is basically a brute force cheat.
    # Though this is solvable via dynamic programming (recursion)
    valid_combi = 0
    valid_arr = []
    for n in range(len(i)):
        for tup in list(combinations(i,n)):
            
            # Part 1
            if sum(tup) == 150:
                valid_combi += 1
                valid_arr.append(tup)
                
    # Part 2
    min_containers_needed = min([len(t) for t in valid_arr])                   
    min_valid_combi = 0
    for t in valid_arr:
        if len(t) == min_containers_needed:
            min_valid_combi +=1

    return valid_combi, min_valid_combi

if __name__ == "__main__":
    input = read("./inputs/day17.txt")
    
    # Part 1
    out, out2 = get_combinations(input)
    print(out)

    # Part 2
    print(out2)
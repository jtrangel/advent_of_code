from itertools import permutations
import numpy as np

# Read input txt file
def read(path):
    return open(path, "r").read()

#----------------------------------------------------------------------
# Part 1 (and 2) Code

def check_routes(input):
    places = set()
    distances = {}
    routes = []
    path_lengths = []
    
    for line in input.splitlines():
        n = line.split(" ")

        ## Store unique places and the distances between places
        places.add(n[0])
        places.add(n[2])

        ## Create dictionary of possible paths and the corresponding distance
        distances[f"{n[0]}{n[2]}"] = n[-1]
        distances[f"{n[2]}{n[0]}"] = n[-1]
    
    # Generate all possible routes
    routes = list(permutations(places))
    # Testing invalid path
    routes.append(("john","cena"))
    routes.append(("john","cena2"))

    ##
    ## For all routes, check the distances between each step and sum.
    ## Store all sums into `path_lengths`. If path is not valid, the 
    ## route is not considered and a path length of 99999 is appended 
    ##

    for route in routes:
        path_length = 0
        for n in range(len(route)-1):
            path = route[n] + route[n+1] 
            if path in distances:
                path_length += int(distances[path])
            else:
                path_length = 99999
                print(f"Path does not exist: {path}")
                break
        path_lengths.append(path_length)
    
    ## For part 1
    # return min(path_lengths)

    ## For part 2, getting max path length via this return instead.
    ## Rest of the code stays the same.
    return max([n for n in path_lengths if n != 99999 ])

if __name__ == "__main__":
    input = read("./inputs/day9.txt")

    ## Part 1
    # output = check_routes(input)
    # print(output)

    ## Part 2
    output = check_routes(input)
    print(output)
# Read input txt file
def read(path):
    file_path = path

    with open(file_path, "r") as file:
        input = file.read()

    # print(input)
    print(len(input))
    return input

def floor_check(input):
    floor = 0
    idx = 1
    for n in input:
        idx+=1
        if n == "(":    
            floor+=1
        else:
            floor-=1

        ## Code for Part 2

        if floor == -1:
            # print(floor)
            # print(idx)
            break

    ## Part 1    
    # return floor

    # Part 2
    return idx

def main():
    input = read("./inputs/day1.txt")
    # Test input
    # input = "((("
    floor = floor_check(input)
    print(floor)

if __name__ == "__main__":
    main()
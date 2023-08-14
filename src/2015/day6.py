import re

# Read input txt file
def read(path):
    file_path = path

    with open(file_path, "r") as file:
        input = file.read()

    return input

#----------------------------------------------------------------------
# Part 1 Code

def follow(input):

    arr = [[0 for i in range(1000)] for j in range(1000)]

    for line in input.splitlines():

        # Parse integer corner points from input text
        # These are used as the ranges for doing changes below
        nums = [int(n) for n in re.findall(r'\d+', line)]

        # Swap value if toggle
        if re.search('toggle', line):   
            for m in range(nums[0],nums[2]+1):
                for n in range(nums[1],nums[3]+1):
                    if arr[m][n] == 0:
                        arr[m][n] = 1
                    else:
                        arr[m][n] = 0
        # Set to 1 if turn on, to 0 if turn off
        else:
            if re.search('turn on', line):
                val = 1
            elif re.search('turn off', line):
                val = 0

            for m in range(nums[0],nums[2]+1):
                for n in range(nums[1],nums[3]+1):
                        arr[m][n] = val

    count = sum([num for row in arr for num in row])

    return count

#----------------------------------------------------------------------
# Part 2 Code

def follow2(input):

    arr = [[0 for i in range(1000)] for j in range(1000)]

    for line in input.splitlines():

        nums = [int(n) for n in re.findall(r'\d+', line)]

        # Re-define each keyword meaning
        if re.search('toggle', line):
            val = 2
        elif re.search('turn on', line):
            val = 1
        elif re.search('turn off', line):
            val = -1

        for m in range(nums[0],nums[2]+1):
            for n in range(nums[1],nums[3]+1):
                    arr[m][n] += val

                    # Set minimum value
                    if arr[m][n] <0:
                        arr[m][n] = 0

    count = sum([num for row in arr for num in row])

    return count

if __name__ == "__main__":
    input = read("./inputs/day6.txt")

    ## Part 1
    output = follow(input)
    print(output)

    ## Part 2
    output = follow2(input)
    print(output)
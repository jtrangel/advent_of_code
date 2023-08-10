import hashlib as h

# Read input txt file
def read(path):

    file_path = path

    with open(file_path, "r") as file:
        input = file.read()

    # print(input)
    
    return input

#----------------------------------------------------------------------
# Part 1 and 2 Code

def min_hash(input):

    n = 0
    hex_hash = ""

    ## For part 1 , we check for first 5 to be zeroes. 
    ## For part 2 , we check for first 6 to be zero.
    while hex_hash[0:6] != "000000":
        string = input + str(n)
        n+=1
        hex_hash = h.md5(f'{string}'.encode('utf-8')).hexdigest()

        ## Test code to prevent possible infinite loop
        # print(hex_hash)
        # print(hex_hash[0:5])
        # if n > 50:
        #     break

    return n-1, hex_hash

if __name__ == "__main__":
    input = read("./inputs/day4.txt")

    ## Test cases
    # output, hex = min_hash("abcdef")
    # output, hex = min_hash("pqrstuv")

    output, hex = min_hash(input)
    print(output, hex)
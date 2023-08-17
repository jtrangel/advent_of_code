import re

# Read input txt file
def read(path):
    file_path = path

    with open(file_path, "r") as file:
        input = file.read()

    return input

#----------------------------------------------------------------------
# Part 1 Code

def string_parse_count(input):

    total_character_count = 0
    total_memory_count = 0
    
    for line in input.splitlines():
        total_character_count += len(line)

        ## My manual solution that didnt work lol.
        ## I found that several cases of hex conversion did not work.
        ## \x9e \x9d \x9f \x93 \x97, etc. not sure why. but it skewed
        ## the result and gave me 1327. Whcih is close to the answer of 1342.

        # char = line.strip('""')
        
        # if "\\x" in char:
            # num = char.count("\\x")
            # for n in range(num):
                # # Take index where \x starts and the next 2 characters
                # idx = char.index("\\x")
                # hex = char[idx:idx+4]

                # # Exit condition if x is coincidentally sandwiched, i.e. \\x\\
                # if "\\" in hex[-1] \
                #     or "\\" in hex[-2] \
                #     or (char[idx] == "\\" and char[idx-1] == "\\"): #and char[idx-2] != "\\"):
                #     break

                # # evaluate the hex code and replace it in the main string
                # hex_val = eval('"' + hex + '"')
                # char = char.replace(hex, hex_val)
            
        # if "\\\"" in char:
        #     char = char.replace("\\\"", "\"")
        # if "\\\\" in char:
        #     char = char.replace("\\\\", "\\")

        char = eval(line)

        total_memory_count += len(char)
    
    return total_character_count - total_memory_count


#----------------------------------------------------------------------
# Part 2 Code

def string_parse_count2(input):

    total_character_count = 0
    total_encoded_count = 0
    
    for char in input.splitlines():
        total_character_count += len(char)

        if "\\" in char:
            char = char.replace("\\", "\\\\")
        if "\"" in char:
            char = char.replace("\"", "\\\"")
        
        char = '"' + char + '"'

        total_encoded_count += len(char)
    
    return total_encoded_count - total_character_count

if __name__ == "__main__":
    # input = read("./inputs/test.txt")
    input = read("./inputs/day8.txt")

    ## Part 1
    output = string_parse_count(input)
    print(output)

    # Part 2
    output = string_parse_count2(input)
    print(output)
    
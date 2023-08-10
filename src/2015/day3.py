# Read input txt file
def read(path):

    file_path = path

    with open(file_path, "r") as file:
        input = file.read()

    # print(input)
    
    return input

#----------------------------------------------------------------------
# Part 1 Code

def count(position, input, position_list):

    unique_presents_given = 1

    position_list.append(position.copy())

    for n in input:

        if n == "^":
            position[1] += 1
        if n == "v":
            position[1] -= 1
        if n == ">":
            position[0] += 1
        if n == "<":
            position[0] -= 1    
        
        # If new position, then a unique present has been given
        if position not in position_list:

            unique_presents_given += 1

            # Remember positions
            position_list.append(position.copy())

        else:
            pass

        
        
    return [unique_presents_given, position_list]

#----------------------------------------------------------------------
# Part 2 Code

def count2(input):
    even_actions = []
    odd_actions = []
    idx = 0

    # Separate the instructions for santa and robot santa
    for n in input:
        
        if idx%2 == 0:
            even_actions.append(n)
        else:
            odd_actions.append(n)
        idx +=1

    # Give instructions to both, using the position list of santa as the
    # position list of robo, to mimic a complete position list
    santa_output = count([0,0],even_actions,[])
    robo_output = count([0,0],odd_actions, santa_output[1])

    # Add the unique presents given and offset by 1 since robo and santa have
    # same starting position
    unique_presents_given = santa_output[0] + robo_output[0] - 1 

    return unique_presents_given

if __name__ == "__main__":
    input = read("./inputs/day3.txt")

    ## Part 1
    output = count([0,0], input, [])
    print(output[0])

    ## Part 2
    output = count2(input)
    print(output)
#----------------------------------------------------------------------
# Part 1 (and 2) Code

def generate(input):

    new = ""
    repeats = 0

    ## For checking if end of string/input
    input += "_"
    
    for n in range(len(input)):

        ## repeats tracks the number of times a digit repeats consecutively
        if input[n] != "_":
            if input[n] != input[n+1] and repeats == 0:
                new += f"1{input[n]}"
            elif input[n] != input[n+1] and repeats != 0:
                new += f"{repeats + 1}{input[n]}"
                repeats = 0
            else:
                repeats +=1
        
        # print(n)
        # print(repeats)
        # print(f"new: {new}")
        # print()
            
    return new

## Recurse function
def re_generate(input, iterations):
    for n in range(iterations):
        input = generate(input)

    return len(input)

if __name__ == "__main__":
    input = "1321131112"

    ## Part 1
    output = re_generate(input,40)
    print(output)

    ## Part 2
    output = re_generate(input,50)
    print(output)
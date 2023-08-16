# Read input txt file
def read(path):
    file_path = path

    with open(file_path, "r") as file:
        input = file.read()

    return input

#----------------------------------------------------------------------
# Part 1 (and 2) Code

def circuit(input, **kwargs):

    # signals stores wire:signal key value pairs. 
    # operation_list stores all operations
    # total_wires lists down all the distinct wires
    signals = {}
    operation_list = []
    total_wires = set()

    for line in input.splitlines():

        # break down each line into an array of instructions with predictable indices
        operation = line.replace(" ->", "").split(" ")
        operation_list.append(operation)
        total_wires.add(operation[-1])

        # add initial unary inputs to the string (i.e. 123 -> x)

        if len(operation) == 2 and operation[0].isnumeric():
                signals[operation[-1]] = int(operation[0])

    # Part 2 code for handling manual input
    if kwargs != {}:
        # print(kwargs)
        signals["b"] = kwargs["b"]
    
    # recursively check if new operations are solvable using the current values
    # that are existing in signals. 
    # each operation is handled differently since indices vary
    while len(signals) < len(total_wires):
        for n in operation_list:
            if n[-1] not in signals:
                
                if len(n) == 2 and n[0] in signals:
                    signals[n[-1]] = int(signals[n[0]])

                if n[0] == "NOT" and n[1] in signals:
                    signals[n[-1]] = ~int(signals[n[1]])

                if n[1] == "RSHIFT" and n[0] in signals:
                    signals[n[-1]] = signals[n[0]] >> int(n[2])
                
                if n[1] == "LSHIFT" and n[0] in signals:
                    signals[n[-1]] = signals[n[0]] << int(n[2])
 
                ## For OR and AND, add case by case handling for when
                ## only one of the inputs is necessary.
                if n[1] == "OR":
                    if n[0] in signals and n[2] in signals:
                        signals[n[-1]] = signals[n[0]] | signals[n[2]]
                    elif n[0].isnumeric() and n[2] in signals:
                        signals[n[-1]] = int(n[0]) | signals[n[2]]
                    elif n[0] in signals and n[2].isnumeric():
                        signals[n[-1]] = signals[n[0]] | int(n[2])
                    else:
                        pass
                
                if n[1] == "AND":
                    if n[0] in signals and n[2] in signals:
                        signals[n[-1]] = signals[n[0]] & signals[n[2]]
                    elif n[0].isnumeric() and n[2] in signals:
                        signals[n[-1]] = int(n[0]) & signals[n[2]]
                    elif n[0] in signals and n[2].isnumeric():
                        signals[n[-1]] = signals[n[0]] & int(n[2])
                    else:
                        pass
        # print(len(signals))          
        # print(len(total_wires))

    # print(signals)
    
    return signals['a']

        

if __name__ == "__main__":
    input = read("./inputs/day7.txt")

    ## Part 1
    output = circuit(input)
    print(output)

    ## Part 2
    output = circuit(input, b=16076)
    print(output)
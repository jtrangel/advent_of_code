from typing import Tuple

def read(path: str) -> str:
    return open(path, "r").read()

aunt_data = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def match_aunt(inpt: str) -> Tuple[int, int]:

    # For each line, grab the key value pair known
    for line in inpt.splitlines():
        n = line.split(' ')

        key1 = n[2].rstrip(':')
        val1 = int(n[3].rstrip(','))

        key2 = n[4].rstrip(':')
        val2 = int(n[5].rstrip(','))

        key3 = n[6].rstrip(':')
        val3 = int(n[7].rstrip(','))

        # Part 1: match values to the known values
        if (val1 == aunt_data[key1] and
            val2 == aunt_data[key2] and
            val3 == aunt_data[key3]
            ):
            aunt_num1 = int(n[1].rstrip(':'))

        # Part 2: Set value as lower limit or upper limit for certain keys
        lower_lim = ['cats', 'trees']
        upper_lim = ['pomeranians', 'goldfish']

        ops = []
        for k in [key1, key2, key3]:
            if k in lower_lim:
                operator = ">"
            elif k in upper_lim:
                operator = "<"
            else:
                operator = "=="

            ops.append(operator)

        # Evaluate each condition using the dynamic key assignment
        if (eval(f"val1 {ops[0]} aunt_data[key1]")
            and
            eval(f"val2 {ops[1]} aunt_data[key2]")
            and
            eval(f"val3 {ops[2]} aunt_data[key3]")
            ):
            aunt_num2 = int(n[1].rstrip(':'))

    return aunt_num1, aunt_num2

if __name__ == "__main__":

    inpt = read("./inputs/day16.txt")

    # Part 1
    out1, out2 = match_aunt(inpt)
    print(out1)

    # Part 2
    print(out2)

#----------------------------------------------------------------------
# Part 1 

# Define increment function for strings (single character)
def increment_char(n):
    return chr(ord(n) +1) 

# Generator function that increments rightmost character
# Generator functions only iterate on next() so while True is fine.
def increment_string(str):
    str = list(str)
    while True:
        idx = -1
        while str[idx] == 'z':
            str[idx] = 'a'
            idx -=1
        str[idx] = increment_char(str[idx])
        yield str

## Basis lambda functions for each condition (inspired by narimiran on github)
# has_increasing_straight = lambda pw_nums: (
#     any(a == b-1 == c-2 for a, b, c in zip(pw_nums, pw_nums[1:], pw_nums[2:])))
# has_invalid_letters = lambda pw: any(l in pw for l in "iol")
# has_two_pairs = lambda pw: len({a for a, b in zip(pw, pw[1:]) if a == b}) >= 2

def has_valid_letters(input):
    out = [char not in input for char in "iol"]
    return any(out)

# Function compares the two inputs by pairing each consecutive character 
# into an set of tuples via Zip. Zips are viewable via tuple()
def has_consecutive_same(input):
    # print(input, input[1:])
    # print(tuple(zip(input, input[1:])))
    out = {a for a,b in zip(input, input[1:]) if a == b}
    # True if there are atleast two different non-overlapping pairs of letters
    return len(out) >= 2

def has_increasing_straight(input):
    # Maps out the ord() function for each string in input
    # ins here is a list of unicode numbers representing the string
    ins = list(map(ord,input))
    out = [a == b-1 == c-2 for a,b,c in zip(ins, ins[1:], ins[2:])]
    return any(out)

def re_create(input):
    yield from (''.join(input) for input in increment_string(input) if
                    has_valid_letters(input) and
                    has_consecutive_same(input) and
                    has_increasing_straight(input)
                )
    
if __name__ == "__main__":
    input = "hepxcrrq"

    ## Part 1
    output = re_create(input)
    print(f"next_pass: {next(output)}")

    ## Part 2
    print(f"next_pass2: {next(output)}")


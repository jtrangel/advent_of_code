from itertools import permutations

def read(path):
    return open(path, "r").read()

## Brute force method
# Function to create all possible combinations
def create_permutations_and_scoring(input, part2):
    people = set()
    h_score={}

    ## Part 2 code for adding a new person. Brute force but works nonetheless for now.
    if part2:
        part2_input = \
        """
Alice would gain 0 happiness units by sitting next to Jerico.
Bob would gain 0 happiness units by sitting next to Jerico.
Carol would gain 0 happiness units by sitting next to Jerico.
David would gain 0 happiness units by sitting next to Jerico.
Eric would gain 0 happiness units by sitting next to Jerico.
Frank would gain 0 happiness units by sitting next to Jerico.
Mallory would gain 0 happiness units by sitting next to Jerico.
George would gain 0 happiness units by sitting next to Jerico.
Jerico would gain 0 happiness units by sitting next to Alice.
Jerico would gain 0 happiness units by sitting next to Bob.
Jerico would gain 0 happiness units by sitting next to Carol.
Jerico would gain 0 happiness units by sitting next to David.
Jerico would gain 0 happiness units by sitting next to Eric.
Jerico would gain 0 happiness units by sitting next to Frank.
Jerico would gain 0 happiness units by sitting next to George.
Jerico would gain 0 happiness units by sitting next to Mallory.
"""

        input += input + part2_input

    for line in input.splitlines():
        n = line.split(" ")
        # List all distinct people
        people.add(n[0])
    
        if n[2] == 'gain':
            h_score[f"{n[0]}-{n[-1].rstrip('.')}"] = int(n[3])
        else:
            h_score[f"{n[0]}-{n[-1].rstrip('.')}"] = -int(n[3])

    
    perms = list(permutations(people))
    
    return people, perms, h_score

def optimize(people, perms, scores):
    
    max_happ = 0
    for m in perms:
        # Get total happiness in arrangement
        happ = 0
        for idx, n in enumerate(m):
            if idx < len(people) -1:
                p1 = m[idx]
                p2 = m[idx + 1]
            else: 
                p1 = m[idx]
                p2 = m[0]
            happ += scores[f"{p1}-{p2}"] + scores[f"{p2}-{p1}"]
            if happ > max_happ:
                max_happ = happ

    return max_happ

if __name__ == "__main__":
    input = read("./inputs/day13.txt")

    # Part 1 
    people, perms, scores = create_permutations_and_scoring(input, False)
    output = optimize(people, perms, scores)
    print(output)

    # Part 2
    people2, perms2, scores2 = create_permutations_and_scoring(input, True)
    output2 = optimize(people2, perms2, scores2)
    print(output2)
from typing import List, Set
import re
from random import shuffle

def read(path: str) -> str:
    return open(path, "r").read()

def get_replacements(r: str) -> List[List]:

    d = []
    for n in r.splitlines():
        n = n.split(' ')
        d.append([n[0], n[-1]])

    return d

def get_distinct_molecules(rule_list: List[List], target: str) -> Set:

    distinct_molecules = set()
    for n in rule_list:
        replace_count = len(re.findall(n[0], target))
        for idx in range(replace_count):
            new_str = replace_nth(n[0], n[1], target, idx + 1)
            distinct_molecules.add(new_str)

    return distinct_molecules

def replace_nth(sub: str, repl: str, txt: str, nth: int) -> str:
    arr = txt.split(sub)
    part1 = sub.join(arr[:nth])
    part2 = sub.join(arr[nth:])

    return part1 + repl + part2

def backtrack_molecule(rule_list: List[List], target: str) -> int:

    # Solution inspired from Reddit. Couldn't solve on my own due to complexity.
    tgt = target
    steps = 0
    while tgt != 'e':
        tmp = tgt
        for n in rule_list:
            if n[1] not in tgt:
                continue

            tgt = tgt.replace(n[1], n[0], 1)
            steps += 1

        # Never had to reach this part of the loop
        if tmp == tgt:
            print('shuffling')
            steps = 0
            shuffle(rule_list)

    return steps

if __name__ == "__main__":
    inpt = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"
    inpt_rules = read("./inputs/day19.txt")
    rules = get_replacements(inpt_rules)

    # Part 1
    out = sum([1 for n in get_distinct_molecules(rules, inpt)])
    print(out)

    # Part 2
    out2 = backtrack_molecule(rules, inpt)
    print(out2)


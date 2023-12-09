from typing import Dict, List

def read(path:str) -> str:
    return open(path, "r").read()

def get_attributes(input:str) -> List:

    # Store each ingredient as a dictionary
    ingredients = []
    for line in input.splitlines():
        n = line.split(" ")
        
        # Dynamically instantiate variable names for each ingredient
        globals()[n[0].rstrip(':')] = {
            n[1] : int(n[2].rstrip(',')),
            n[3] : int(n[4].rstrip(',')),
            n[5] : int(n[6].rstrip(',')),
            n[7] : int(n[8].rstrip(',')),
            n[9] : int(n[10].rstrip(','))
        }

        ingredients.append(n[0].rstrip(':'))

    return ingredients

def get_score(a: Dict, b: Dict, c: Dict, d:Dict) -> int:

    # For each possible comination, calculate the score
    max_score = 0
    curr_score = 0
    max_calorie_score = 0
    for n1 in range(0, 101):
        for n2 in range(0, 101-n1):
            for n3 in range (0, 101-n1-n2):
                for n4 in range (0, 101-n1-n2-n3):
                    if n1 + n2 + n3 + n4 == 100:
                       cap =  n1*a['capacity'] + n2*b['capacity'] + n3*c['capacity'] + n4*d['capacity']
                       dur =  n1*a['durability'] + n2*b['durability'] + n3*c['durability'] + n4*d['durability']
                       flav = n1*a['flavor'] + n2*b['flavor'] + n3*c['flavor'] + n4*d['flavor']
                       text = n1*a['texture'] + n2*b['texture'] + n3*c['texture'] + n4*d['texture']
                       cals = n1*a['calories'] + n2*b['calories'] + n3*c['calories'] + n4*d['calories']

                       if cap >0 and dur>0 and flav>0 and text>0:
                        curr_score = cap*dur*flav*text
                       else:
                        curr_score = 0
                       
                       if curr_score > max_score:
                        max_score = curr_score

                       # Part 2 condition and output
                       if cals == 500 and curr_score > max_calorie_score:
                        max_calorie_score = curr_score
    return max_score, max_calorie_score                      

if __name__ == "__main__":
    input = read("./inputs/day15.txt")

    ings = get_attributes(input)
    score, cal_score = get_score(eval(f"{ings[0]}"),
              eval(f"{ings[1]}"),
              eval(f"{ings[2]}"),
              eval(f"{ings[3]}")
              )
    print(score, cal_score)


    

import re
import json

# Read input txt file
def read(path):
    return open(path, "r").read()

def extract_ints(input:str) -> []:
    return list(map(int, re.findall(r'-?\d+', input)))

# Tried regex but failed, will do solution with json package instead
# def get_objects(input:str) -> []:
#     return list(map(str, re.findall(r'\{(.*?):"red"(.*?)\}', input)))

# def list_to_string(input:[]) -> str:
#     return ''.join(str(x) for x in input)

def red_val_check(obj) -> {}:
    if "red" in obj.values():
        return {}
    else: 
        return obj

if __name__ == "__main__":
    input = read("./inputs/day12.txt")
    
    ## Part 1
    output = sum(extract_ints(input))
    print(output)

    ## Part 2
    # Failed attempt
    # objs = get_objects(input)
    # objs_str = list_to_string(objs)
    
    # extra = sum(extract_ints(objs_str))
    # print(output - extra)

    objs = json.loads(input, object_hook=red_val_check)
    
    output = sum(extract_ints(str(objs)))
    print(output)
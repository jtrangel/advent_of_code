def read(path: str) -> str:
    return open(path, "r").read()

def get_total_presents(house_num: int, mult: int, part2: bool) -> int:
    """
    Gets total presents via all prime factors of a number

    Args:
        part2 (bool): if part 2, use other return statement
        mult (int): present multiplier
        house_num (int): house number

    Returns:
        int: total number of presents received by that house
    """
    factors = []
    # If the elf number is a divisor, it visits the house

    for n in range(1, house_num + 1):
        if house_num % n == 0:
            factors.append(n)
    if part2:
        return mult*sum([x for x in factors if house_num/x <= 50])
    else:
        return mult*sum(factors)

def determine_min_house_num(n: int, mult: int, part2: bool) -> int:
    """
    Fuction to count number of presents obtained by a given house number

    Args:
        part2 (bool): if part 2 use different sum method
        mult (int): present multiplier
        n (int): minimum present number

    Returns:
        int: house number
    """
    presents_curr: int = 0
    # Lower limit based on previous runs
    house_num: int = 750000
    # house_num: int = 0

    # Increase house number while checking if total presents is
    # atleast higher than minimum. Reddit insight that every
    # 6 houses the total presents spikes. So iterating w/ that instead
    while presents_curr <= n:
        house_num += 6
        presents_curr = get_total_presents(house_num, mult, part2)

        if house_num % 1000 == 0:
            print(house_num)
            print(presents_curr)

    return house_num

if __name__ == '__main__':
    inpt: int = 33100000

    # Part 1
    # outpt = determine_min_house_num(inpt, 10, False)
    # print()
    # print(outpt)

    # Part 2
    outpt = determine_min_house_num(inpt, 11, True)
    print()
    print(outpt)

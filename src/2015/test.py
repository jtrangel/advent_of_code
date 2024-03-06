input = 33100000

def get_factors(n):
    x = 1
    factors = []
    while x ** 2 <= n:
        if n % x == 0:
            factors.append(x)
            factors.append(n / x)
        x += 1
    return factors

for n in range(6, 6000000, 6):
    print (n, sum(get_factors(n)))
    if(10 * sum(get_factors(n))) >= input:
        print(n)
        break
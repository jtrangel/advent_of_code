## Function that determines if a string is a palindrome
# racecar

def reverse(input:str) -> str:
    out = []
    for n in range(len(input)):
        out.append(input[-(n+1)])
    return out
     

def palindrome_check(input:str) -> bool:
    reversed = reverse(input)
    i=0
    for n in input:
        if n == reversed[i]:
            pass
        else:
            return False
        i+=1
    return True

if __name__ == "__main__":
    print(reverse("word"))
    print(palindrome_check("racecar"))
    print(palindrome_check("madam"))
    print(palindrome_check("madams"))

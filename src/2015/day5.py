import pandas as pd
import numpy as np

# Read input file
def read():

    input = pd.read_csv("./inputs/day5.txt",
                        engine = "pyarrow",
                        header=None)
    input.columns = ["string"]

    ## To check dataframe state
    # print(input.describe)

    return input

#----------------------------------------------------------------------
# Part 1 Code

def check_if_nice(input):

    ## Filter based on vowel count
    input["vowel_count"] = input["string"].str.count("a|e|i|o|u")

    df1 = input[input["vowel_count"] >= 3].copy()
    # print(df1.describe)

    ## Filter based on disallowed substrings
    df2 = df1[~df1["string"].str.contains('ab|cd|pq|xy')].copy()
    # print(df2.describe)

    ## Filter based on # of consecutive duplicate strings (via regex)
    df2["duplicates"] = df2["string"].str.count(r'(.)\1+')
    df3 = df2[df2["duplicates"] > 0].copy()
    # print(df3.describe)

    return df3.count()

#----------------------------------------------------------------------
# Part 2 Code

def check_if_nice2(df):

    ## Filter based on 2 of consecutive non overlapping duplicate strings (via regex)
    df["duplicates"] = df["string"].str.count(r'(..)(?=.*\1)')
    df2 = df[df["duplicates"] > 0].copy()
    # print(df2.describe)

    ## Filter based on containing a repeating letter that sandwiches exactly 1 letter in between i.e (xxyx -> xyx, asdfgf -> fgf)
    df2["duplicates2"] = df["string"].str.count(r'(.).\1')
    df3 = df2[df2["duplicates2"] > 0].copy()
    # print(df3.describe)

    return df3.count()

if __name__ == "__main__":
    input = read()

    ## Part 1
    # output = check_if_nice(input)
    # print(output)

    # Part 2
    output = check_if_nice2(input)
    print(output)
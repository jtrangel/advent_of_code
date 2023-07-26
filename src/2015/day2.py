import pandas as pd
import numpy as np

# Read input file
def read():

    input = pd.read_csv("./inputs/day2.txt",
                        sep = "x",
                        engine = "pyarrow",
                        header=None)
    input.columns = ["l","w","h"]

    ## To check dataframe state
    # print(input.head())

    return input

#----------------------------------------------------------------------
# Part 1 Code

def surface_area(l,w,h):
    
    return 2*(l*w +w*h + h*l)

def aggregate(input):
    
    input["surface_area"] = surface_area(input.l, input.w, input.h)

    # Df for extra wrapper needed
    extra = pd.DataFrame()
    extra["lw"] = input.l*input.w
    extra["wh"] = input.w*input.h
    extra["hl"] = input.h*input.l

    extra["extra_wrapper"] = extra.min(axis = 1)

    ## To check dataframe state
    # print(extra.head())

    total_wrapper = input["surface_area"].sum() +extra["extra_wrapper"].sum()

    ## To check dataframe state
    # print(input.head())

    output = total_wrapper

    return output

#----------------------------------------------------------------------
# Part 2 Code

def ribbon_length(input):

    ## Sort the data per row then transpose to intake as columns in df
    input['lowest'], input['second_lowest'] = np.sort(input, axis = 1)[:, :2].T
    
    ## Get the component sums of ribbon length
    input['ribbon_wrap'] = 2*(input['lowest'] + input['second_lowest'])

    input['ribbon_bow'] = input.l * input.w * input.h

    print(input.head())

    total_ribbon_length = input['ribbon_wrap'].sum() + input['ribbon_bow'].sum()

    return total_ribbon_length

if __name__ == "__main__":
    input = read()

    ## Part 1 output
    # output = aggregate(input)
    # print(output)

    ## Part 2 output
    # output = ribbon_length(input)
    # print(output)
import itertools
import functools
import re

excluded = ['.','_','\n']

def checkSymbol(char: str):
    return (not char.isnumeric()) and char not in excluded
    
def convert(char):
    if checkSymbol(char):
        return char
    else:
        return "_"


def checkAround(pos,grid):
    for i in range(-1,2):
        for j in range(-1,2):
            r = pos[0] + i
            c = pos[1] + j
            if (r >= 0 and r < len(grid)) and (c >= 0 and c < len(grid[r])):
                char = grid[r][c]
                if checkSymbol(char):
                    print(char)
                    return True
    return False


def process_input():
    total = 0
    
    with open('input.txt','r') as f:
        lines = f.readlines()


        #print(checkAround((104,139),symbols))
        valid = False
        curr = ""
        
        for l in range(0,len(lines)):
            for c in range(0,len(lines[l])):
                char = lines[l][c]
                if char.isnumeric():
                    curr += char
                    if checkAround((l,c),lines):
                        valid = True
                elif curr != "":
                    if valid == True:
                        val = int(curr)
                        total += val
                        #print(val)
                        
                    valid = False
                    curr = ""
                
    return total
 
result = process_input()
print(result)

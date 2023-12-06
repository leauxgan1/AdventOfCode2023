

def checkGear(char: str):
    return char == "*"
    
def convert(char):
    if checkGear(char):
        return char
    else:
        return "_"

total = 0
with open("input.txt","r")as f:
    lines = f.readlines()

    symbols = list(map(lambda line: list(map(lambda char: convert(char),line)),lines))
    print(symbols)

    for l in range(len(lines)):
        curr = ""
        for c in range(len(lines)):
            valid = False 
            char = lines[l][c]

print(total)

import os
import functools
import time 


def process_input():
    total = 0
    reds = 12
    greens = 13
    blues = 14
    
    with open('input.txt','r') as f:
        lines = f.readlines()
        for l in range(len(lines)):
            first = lines[l].split(':')
            id = l + 1
            roundData = [s.strip() for s in first[1].split(";")]
            gameData = [s.split(",") for s in roundData]
            maxes = [0,0,0] # R G B
            valid = True
            for round in range(0,len(gameData)):
                for item in gameData[round]:
                    stripped = item.strip()
                    parts = stripped.split(" ")
                    print(parts)
                    val = int(parts[0])

                    color = parts[1]
                    if color == "red":
                        if val > maxes[0]:
                            maxes[0] = val
                    elif color == "green":
                        if val > maxes[1]:
                            maxes[1] = val
                    elif color == "blue":
                        if val > maxes[2]:
                            maxes[2] = val
                    else:
                        raise ValueError
            print(maxes)
            power = maxes[0] * maxes[1] * maxes[2]
            total += power

    return total
 
result = process_input()
print(result)

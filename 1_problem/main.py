import os
import functools
import time 
import trace
import re



def conv_to_int(s):
    match s:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
    return s


def process_input():
    total = 0
    with open('input.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            left =  re.search("(one|two|three|four|five|six|seven|eight|nine|[0-9])",line).group(0)
            right = re.search("(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9])",line[::-1]).group(0)
            if left and right:
                first = conv_to_int(left)
                second = conv_to_int(right[::-1])
                joined = "".join([first,second])
                total += int(joined)
            else:
                first = conv_to_int(left)
                total += int(joined)
    return total
 
startTime = time.time()

result = process_input()

diff = time.time() - startTime

print(diff)

print(result)

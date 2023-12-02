import time

forwardsNameMapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
backwardsNameMapping = {
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}
def read_calibrations():
    total = 0
    with open("input.txt") as f:
        for line in f.readlines():
            nums = []
            curr_str = ""
            # Search forward through the string, escaping early on integer literals or found string literals of integers (one,two,three...)
            for char in line:
                if char.isnumeric():
                    nums.append(char)
                curr_str += char
                for key in forwardsNameMapping.keys():
                    if key in curr_str:
                        nums.append(forwardsNameMapping[key])
                if len(nums) > 0:
                    break
            
            # Repeat previous step, checking in the opposite direction
            curr_str = ""
            for char in line[::-1]:
                if char.isnumeric():
                    nums.append(char)
                curr_str += char
                for key in backwardsNameMapping.keys():
                    if key in curr_str:
                        nums.append(backwardsNameMapping[key])
                if len(nums) > 1:
                    break
        print(nums)
        if len(nums) > 0: 
            joined = int("".join((nums[0],nums[-1])))
            total += joined
    return total

start = time.time()

total = read_calibrations()

diff = time.time() - start
print(total, diff)


        

        

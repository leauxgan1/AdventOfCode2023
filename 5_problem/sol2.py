import itertools
import functools
from icecream import ic
import re



class Mapping():
    def __init__(self,destinations,sources,lengths):
        self.destinations = destinations
        self.sources = sources
        self.lengths = lengths

    def convert(self,val):
        for source, destination, length in zip(self.sources,self.destinations,self.lengths):
            if val >= source and val < source + length:
                return destination + (val - source)
        else:
            return val
        
    def convertMany(self,vals):
        return [self.convert(val) for val in vals]

def process_input():
    lowest = 10000000
    mappings = []
    mappingsVals = []

    with open('test.txt','r') as f:
        lines = f.read()
        formatted = re.split(r"[\n]+",lines)
        ic(formatted)
        curr = []
        seedRanges = list(map(lambda s: int(s), formatted[1].split(" ")))
        ic(seedRanges)
        seedVals = []
        for s in range(0,len(seedRanges),2):
            for i in range(seedRanges[s],seedRanges[s + 1]):
                seedVals.append(i)
        ic(seedVals)
        # for item in formatted[3:]:
        #     if len(item) < 1:
        #         continue
        #     elif item[-1] == ":":
        #         mappingsVals.append(curr)
        #         curr = []
        #     else:
        #         vals = list(map(lambda s: int(s), item.split(" ")))
        #         curr.append(vals)
        # mappingsVals.append(curr)
        # ic(mappingsVals)
        # for vals in mappingsVals:
        #     if len(vals) == 1:
        #         mappings.append(Mapping([vals[0]], [vals[1]],[vals[2]]))
        #     else:
        #         dests = []
        #         sources = []
        #         lengths = []
        #         for val in vals:
        #             dests.append(val[0])
        #             sources.append(val[1])
        #             lengths.append(val[2])
        #         mappings.append(Mapping(dests, sources,lengths))
                
        # #ic(seedVals)
        # prev = seedVals
        # #ic(len(mappings))
        # for i in range(len(mappings)):
        #     next = mappings[i].convertMany(prev)
        #     prev = next
        #     ic(next)
        # print(min(next))
        


                    

        


        
    return lowest
 
result = process_input()
print(result)

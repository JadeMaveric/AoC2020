"Find two numbers in the list that add up to 2020, return their product"

import bisect

with open('input.txt') as numbers:
    data = [int(x) for x in numbers.read().split('\n')]
    data.sort()

for num in data:
    comp = 2020 - num
    
    if data[bisect.bisect(data, comp)-1] == comp: # binary search
        print(num * comp)
        exit(0)

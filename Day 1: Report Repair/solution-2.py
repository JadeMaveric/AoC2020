"Find two numbers in the list that add up to 2020, return their product"

import bisect

with open('input.txt') as numbers:
    data = [int(x) for x in numbers.read().split('\n')]
    data.sort()

def search(target):
    for num in data:
        comp = target - num
        
        if data[bisect.bisect(data, comp)-1] == comp: # binary search
            return (num, comp)

for num in data:
    target = 2020 - num
    nums = search(target)

    if nums:
        print(num, *nums)
        print(num * nums[0] * nums[1])
        exit(0)

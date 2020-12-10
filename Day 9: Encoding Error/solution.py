PREAMBLE_LENGTH = 25

with open('input') as datafile:
    data = datafile.read()
    data = [int(x) for x in data.strip().split('\n')]

def is_sum(target, arr):
    arr.sort()
    for num in arr:
        if target-num in arr:
            return True
    return False
    

idx = PREAMBLE_LENGTH
for idx, num in enumerate(data[PREAMBLE_LENGTH:]):
    if not is_sum(num, data[idx:idx+PREAMBLE_LENGTH]):
        print(num)
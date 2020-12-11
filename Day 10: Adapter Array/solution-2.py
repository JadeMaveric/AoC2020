with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [int(x) for x in data]

data.append(0)
data.sort()
data.append(data[-1]+3)
plug_count = 0

def memoize(f):
    memo = {}
    def helper(x,y):
        if (x,y) not in memo:
            memo[(x,y)] = f(x,y)
        return memo[(x,y)]
    return helper

@memoize
def count(joltage, curr_idx):
    global data, plug_count
    curr = data[curr_idx]
    if curr == data[-1] and 0 <= curr - joltage <= 3:
        return 1
    elif 0 <= curr - joltage <= 3:
        # Include plug + Exclude plug
        return count(curr, curr_idx+1) + count(joltage, curr_idx+1)
    else:
        return 0

print(count(0,1))


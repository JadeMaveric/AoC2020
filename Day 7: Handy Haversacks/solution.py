# 1. Create the adjency matrix for the bags
# 2. Work backwards to see which bags can fit our sophisticated bag

import numpy as np

with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    #data = [(bagtype, [(num, bagtype),...]), ...]
    data = [line.split(' bags contain ') for line in data]
    data = [(bagtype, [(int(c.split()[0]), ' '.join(c.split()[1:3])) for c in content.split(', ') if c[0] != 'n']) for (bagtype, content) in data]

bagtypes = [entry[0] for entry in data]

# 1.
N = len(bagtypes)
adjmat = np.zeros((N,N), dtype=int)

for row, entry in enumerate(data):
    for count, bag in entry[1]:
        col = bagtypes.index(bag)
        adjmat[row,col] = count

# 2.
ptr = 0
adjmat = adjmat.transpose()
compatible = list(np.where(adjmat[bagtypes.index('shiny gold')] != 0)[0])

while ptr < len(compatible):
    bagnum = compatible[ptr]
    # print('Checking for', bagtypes[bagnum])
    for bag in np.where(adjmat[bagnum] != 0)[0]:
        # print(ptr, bagnum, bagtypes[bagnum], bagtypes[bag])
        if bag not in compatible:
            compatible.append(bag)
    ptr += 1

print(len(compatible))#, compatible)

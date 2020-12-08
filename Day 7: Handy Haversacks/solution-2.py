# 1. Create the adjency matrix for the bags
# 2. Work forwards to see which bags should be fit into our shiny golden bag

import numpy as np

with open('input-demo-2') as datafile:
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
def how_many_bags(bagnum, rec_guard):
    if rec_guard == 0:
        return 0
    # print(rec_guard, "Checking", bagtypes[bagnum])
    if np.all(adjmat[bagnum] == 0):
        return 1
    ans = 0
    for bag, count in enumerate(adjmat[bagnum]):
        ans += count * how_many_bags(bag, count)

    return ans


total = 0
for bag, count in enumerate(adjmat[bagtypes.index('shiny gold')]):
    total += count * how_many_bags(bag, count)

print(total)

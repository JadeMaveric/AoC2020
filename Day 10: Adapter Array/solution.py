with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [int(x) for x in data]

data.sort()
diff = [1,1,1,1]

for a,b in zip(data[:-1], data[1:]):
    diff[abs(a-b)] += 1

print(diff)
print(diff[1] * diff[3])

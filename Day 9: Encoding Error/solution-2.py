import numpy as np

PREAMBLE_LENGTH = 25

with open('input') as datafile:
    data = datafile.read()
    data = [int(x) for x in data.strip().split('\n')]

arr = np.array(data)
a = arr.copy()
b = arr.copy()
target = 32321523

a = a[:-1]; b = b[1:]
a += b
idx = 2

while not target in a:
    a = a[:-1]; b = b[1:]
    a += b
    idx += 1

start = np.where(a == target)[0][0]
end = start + idx
print(np.min(arr[start:end]) + np.max(arr[start:end]))

import numpy as np
from math import sin, cos, pi

with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [(line[0], int(line[1:])) for line in data]

postn = [0,0]
dirct = 0 # East
DEG = pi / 180

for ins, val in data:
    if ins == 'N':
        postn[1] += val
    elif ins == 'S':
        postn[1] -= val
    elif ins == 'E':
        postn[0] += val
    elif ins == 'W':
        postn[0] -= val
    elif ins == 'F':
        postn[0] += val * cos(dirct * DEG)
        postn[1] += val * sin(dirct * DEG)
    elif ins == 'R':
        dirct -= val
    elif ins == 'L':
        dirct += val
    else:
        print("Invalid", ins, val)
        exit()

print(postn)
print(sum(abs(x) for x in postn))


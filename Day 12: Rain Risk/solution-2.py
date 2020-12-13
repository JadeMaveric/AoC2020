import numpy as np
from math import sin, cos, pi

with open('input-demo') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [(line[0], int(line[1:])) for line in data]

postn = [0,0]
waypt = [0,10]
dirct = 0 # East
DEG = pi / 180

for ins, val in data:
    print(ins, val)
    print(postn, waypt)
    input()
    if ins == 'N':
        waypt[1] += val
    elif ins == 'S':
        waypt[1] -= val
    elif ins == 'E':
        waypt[0] += val
    elif ins == 'W':
        waypt[0] -= val
    elif ins == 'F':
        postn[0] += val*waypt[0]
        postn[1] += val*waypt[1]
    elif ins == 'R':
        tempt = waypt.copy()
        waypt[0] = tempt[0] * cos(val * DEG) + tempt[1] * sin(val * DEG)
        waypt[1] = -tempt[0] * sin(val * DEG) + tempt[1] * cos(val * DEG)
    elif ins == 'L':
        val = -val
        tempt = waypt.copy()
        waypt[0] = tempt[0] * cos(val * DEG) + tempt[1] * sin(val * DEG)
        waypt[1] = -tempt[0] * sin(val * DEG) + tempt[1] * cos(val * DEG)
    else:
        print("Invalid", ins, val)
        exit()

print(postn)
print(sum(abs(x) for x in postn))


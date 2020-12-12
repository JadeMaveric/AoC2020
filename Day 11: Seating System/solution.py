import numpy as np

def ncount(row, col):
    global width, height, seats
    neighbours = 0
    for x,y in np.ndindex(3,3):
        x -= 1; y -= 1
        if (0 <= row+x < width) and (0 <= col+y < height) and not (x==0 and y==0):
            neighbours += seats[row+x][col+y] == ord('#')
    return neighbours

with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [[ord(x) for x in line] for line in data]

width = len(data)
height = len(data[0])
_seats = np.array(data)
seats = np.zeros(_seats.shape)
# seats = _seats.copy()
# print(seats)
# print(ncount(0,0))
# exit()

while not np.all(seats == _seats):
    seats = _seats.copy()
    for x,y in np.ndindex(width, height):
        if seats[x][y] == ord('L') and ncount(x,y) == 0:
            _seats[x][y] = ord('#')
        elif seats[x][y] == ord('#') and ncount(x,y) >= 4:
            _seats[x][y] = ord('L')
    # for line in _seats:
    #     print(''.join([chr(x) for x in line]))
    # input()
print([len(x) for x in np.where(seats==ord('#'))])

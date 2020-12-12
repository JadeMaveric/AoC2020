import numpy as np

def ncount(row, col):
    """
    Just like the first solution, but we add a multiplier to the directions
    This lets us count as far as we want. Knowing which loop to put the multiplier in
    is important. Putting it in the inner most one, lets us break out of the loop once we
    find a chair
    """
    global width, height, seats
    # print(row, col, width, height)
    neighbours = [False for i in range(8)]
    direction = {(-1,-1): 0, (-1,0): 1, (-1,1): 2, (0,-1): 3, (0,1): 4, (1,-1): 5, (1,0): 6, (1,1): 7}
    for x,y in np.ndindex(3,3):
        x -= 1; y -= 1
        a,b = x,y
        for multiplier in range(1, max(width,height)):
            # print(x,y,multiplier)
            x = a * multiplier; y = b * multiplier
            if (0 <= row+x < width) and (0 <= col+y < height) and not (x==0 and y==0):
                # print(row+x,col+y,seats[row+x,col+y])
                # input()
                i = direction[(a,b)]
                if seats[row+x][col+y] == ord('#') or seats[row+x][col+y] == ord('L'):
                    # print("Fount one!")
                    neighbours[i] = seats[row+x][col+y] == ord('#')
                    break
    return len(np.where(np.array(neighbours)==True)[0])

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
# print(ncount(3,3))
# exit()

while not np.all(seats == _seats):
    seats = _seats.copy()
    for x,y in np.ndindex(width, height):
        if seats[x][y] == ord('L') and ncount(x,y) == 0:
            _seats[x][y] = ord('#')
        elif seats[x][y] == ord('#') and ncount(x,y) >= 5:
            _seats[x][y] = ord('L')
    # for line in _seats:
    #     print(''.join([chr(x) for x in line]))
    # input()
print([len(x) for x in np.where(seats==ord('#'))])

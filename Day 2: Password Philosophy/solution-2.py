with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [line.split(' ') for line in data]
    data = [(tuple(int(x) for x in a.split('-')), b[0], c) for a,b,c in data]

valid_passwords = 0

for policy in data:
    (low,high),char,password = policy
    is_low = password[low-1] == char
    is_high = password[high-1] == char
    valid_passwords += (is_low and not is_high) or (not is_low and is_high) # is_low XOR is_high

print(valid_passwords)
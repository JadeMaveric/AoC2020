with open('input') as datafile:
    data = datafile.read()
    data = data.strip().split('\n')
    data = [line.split(' ') for line in data]
    data = [(tuple(int(x) for x in a.split('-')), b[0], c) for a,b,c in data]

valid_passwords = 0

for policy in data:
    (low,high),char,password = policy
    valid_passwords += low <= password.count(char) <= high

print(valid_passwords)
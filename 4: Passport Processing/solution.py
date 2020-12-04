import re

# Passport fields are space/new-line separated
regex = re.compile("\n| ")

with open('input-4.txt') as batchfile:
    batchdata = batchfile.read()
    # Passports are separated by an empty line
    entries = [regex.split(entry) for entry in batchdata.split('\n\n')]

passports = 0 # Counter
fields = 0 # Bitfield

for entry in entries:
    fields = 0
    for param in entry:
        field = param[:3]
        if field == 'byr':
            fields |= 1
        if field == 'iyr':
            fields |= 2
        if field == 'eyr':
            fields |= 4
        if field == 'hgt':
            fields |= 8
        if field == 'hcl':
            fields |= 16
        if field == 'ecl':
            fields |= 32
        if field == 'pid':
            fields |= 64
        # if field == 'cid':
        #     entry |= 128

    passports += fields == 127

print(passports)

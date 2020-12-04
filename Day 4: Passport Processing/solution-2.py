import re

# Passport fields are space/new-line separated
regex = re.compile("\n| ")

with open('input-4.txt') as batchfile:
    batchdata = batchfile.read()
    # Passports are separated by an empty line
    entries = [regex.split(entry) for entry in batchdata.split('\n\n')]

passports = 0 # Counter
fields = 0 # Bitfield

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

for entry in entries:
    fields = 0
    for param in entry:
        field = param[:3]
        if field == 'byr':
            try:
                data = int(param[4:])
            except:
                continue
            if 1920 <= data <= 2002:
                fields |= 1
        if field == 'iyr':
            try:
                data = int(param[4:])
            except:
                continue
            if 2010 <= data <= 2020:
                fields |= 2
        if field == 'eyr':
            try:
                data = int(param[4:])
            except:
                continue
            if 2020 <= data <= 2030:
                fields |= 4
        if field == 'hgt':
            try:
                data = int(param[4:-2])
                unit = param[-2:]
            except:
                continue
            if (unit == 'cm' and 150 <= data <= 193) or (unit == 'in' and 59 <= data <= 76):
                fields |= 8
        if field == 'hcl':
            try:
                data = re.compile('#([0-9]|[a-f]){6}').match(param[4:])
            except:
                continue
            if data:
                fields |= 16
        if field == 'ecl':
            try:
                data = param[4:]
            except:
                continue
            if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                fields |= 32
        if field == 'pid':
            try:
                data = re.compile('[0-9]{9}').match(param[4:])
            except:
                continue
            if data and len(param[4:]) == 9:
                fields |= 64
        # if field == 'cid':
        #     fields |= 128
    print(bin(fields))
    passports += fields == 127

print(passports)

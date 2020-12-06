with open('input') as groups:
    data = groups.read()

groups = [[person for person in group.strip().split('\n')] for group in data.strip().split('\n\n')]

group_set = [set() for x in range(len(groups))]

for idx, group in enumerate(groups):
    group_set[idx] = set(group[0])
    for person in group[1:]:
        group_set[idx] &= set(person)

print(sum([len(x) for x in group_set]))
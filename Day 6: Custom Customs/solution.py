with open('input') as groups:
    data = groups.read()

groups = [[answer for answer in group if answer != '\n'] for group in data.strip().split('\n\n')]

group_set = [set() for x in range(len(groups))]

for idx, group in enumerate(groups):
    for answer in group:
        group_set[idx].add(answer)

print(sum([len(x) for x in group_set]))
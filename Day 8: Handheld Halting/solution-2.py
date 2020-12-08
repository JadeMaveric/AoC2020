with open('input') as inputfile:
    data = inputfile.read()
    data = data.split('\n')[:-1]
    data = [line.split(' ') for line in data]

ins = [[op, int(val), idx+int(val) if op=='jmp' else idx+1, False] for idx,(op,val) in enumerate(data)]

# 1. Determine where we need to land so we get to the end
# 2. Determnie which ins needs to be flipped to get to that point
# 3. Run the program and print acc

candidate_points = [len(ins)]
jmp_points = [x[2] for x in ins]

exit_points = []
while candidate_points:
    target = candidate_points.pop()
    new_points = [idx for idx,point in enumerate(jmp_points) if point == target]
    candidate_points.extend(new_points)
    exit_points.append(target)

idx = 0
acc = 0
changed = False
while idx < len(ins):
    op, val, nxt, visited = ins[idx]
    
    # print(f'Instruction {idx}\t{nxt}\t{idx+1 if op=="jmp" else idx+val if op=="nop" else "---"}\t{op}\t{val}\t{visited}')
    if visited:
        print("Uh oh, something went wrong")
        break

    ins[idx][3] = True
    if op == 'nop':
        # Check if flipping works
        if not changed and idx + val in exit_points:
            idx += val
            changed = True
            # print("Changed")
        else:
            idx += 1
    elif op == 'acc':
        acc += val
        idx += 1
    elif op == 'jmp':
        # Check if flipping works
        if not changed and idx + 1 in exit_points:
            idx += 1
            changed = True
            # print("Changed")
        else:
            idx += val

print(acc)

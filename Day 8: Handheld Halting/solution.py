with open('input') as inputfile:
    data = inputfile.read()
    data = data.split('\n')[:-1]
    data = [line.split(' ') for line in data]

ins = [[op, int(val), False] for (op,val) in data]

idx = 0
acc = 0
while True:
    op, val, visited = ins[idx]
    
    if visited:
        print(acc)
        exit()


    ins[idx][2] = True
    if op == 'nop':
        idx += 1
    elif op == 'acc':
        acc += val
        idx += 1
    elif op == 'jmp':
        idx += val

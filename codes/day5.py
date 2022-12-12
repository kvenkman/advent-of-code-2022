test = True

if test:
    input_file = '../inputs/day5_test'
else:
    input_file = '../inputs/day5_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

# identify line containing stack numbers
for line_count, l in enumerate(lines):
    if '[' not in l:
        break

# Parse input

# Create appropriate number of stacks
n_stacks = max([int(x) for x in l.split()])
stacks = [[] for _ in range(n_stacks)]

# indices corresponding to where box name is specified
idxs = [i for i, x in enumerate(l) if (x!= ' ') and (x!='\n')]

# Populate stacks (bottom to top)
for l in lines[0:line_count][::-1]:
    for i, x in enumerate([l[i] for i in idxs]):
        if x != ' ':
            stacks[i].append(x)

# list containing info about moves
move_count, from_stack, to_stack = [], [], []

for l in lines[line_count+2:]:
    count, ranges = l.split("from")
    move_count.append([int(x.strip()) for x in count.split("move") if x != ''][0])
    ranges = ranges.split("to")
    from_stack.append(int(ranges[0].strip()))
    to_stack.append(int(ranges[1].strip()))

# Part 1
for mc, fs, ts in zip(move_count, from_stack, to_stack):
    for i in range(mc):
        stacks[ts-1].append(stacks[fs-1].pop())

print("".join([s[-1] for s in stacks]))
        

# Part 2
# Populate stacks (bottom to top)
stacks = [[] for _ in range(n_stacks)]
for l in lines[0:line_count][::-1]:
    for i, x in enumerate([l[i] for i in idxs]):
        if x != ' ':
            stacks[i].append(x)

for mc, fs, ts in zip(move_count, from_stack, to_stack):
    substack = "".join(stacks[fs-1][-mc:])

    for c in stacks[fs-1][-mc:]:
        _ = stacks[fs-1].pop()
    for c in substack:
        stacks[ts-1].append(c)
        
print("".join([s[-1] for s in stacks]))
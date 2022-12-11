from collections import deque

test = True

if test:
    input_file = '../inputs/day5_test'
else:
    input_file = '../inputs/day5_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

# identify line containing stack numbers
for i, l in enumerate(lines):
    if '[' not in l:
        break

n_stacks = max([int(x) for x in l.split()])
idxs = [i for i, x in enumerate(l) if (x!= ' ') and (x!='\n')]
print(idxs)
# Part 1 

# Part 2
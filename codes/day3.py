from collections import defaultdict
test = False

if test:
    input_file = '../inputs/day3_test'
else:
    input_file = '../inputs/day3_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

priority_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priority_dict = {}
for i, c in enumerate(priority_str):
    priority_dict[c] = i+1

# Part 1
priority_sum = 0
for l in lines:
    first_half = l[:len(l)//2]
    second_half = l[len(l)//2:]

    for c in first_half:
        if c in second_half:
            break

    priority_sum += priority_dict[c]

print(priority_sum)

# Part 2
priority_sum = 0
for i in range(0, len(lines), 3):

    group_dict = defaultdict(int)
    group_str = lines[i+0].strip() + lines[i+1].strip() + lines[i+2].strip()
    for j in range(3):
        for c in set(lines[j+i].strip()):
            group_dict[c] += 1

    for key, value in group_dict.items():
        if value == 3:
            priority_sum += priority_dict[key]
print(priority_sum)

test = False

if test:
    input_file = '../inputs/day4_test'
else:
    input_file = '../inputs/day4_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

# Part 1
full_overlap = 0

for l in lines:
    r1, r2 = l.strip().split(',')
    r11, r12 = [int(x) for x in r1.split('-')]
    r21, r22 = [int(x) for x in r2.split('-')]

    # So that r11 is always <= r21
    if r21<r11:
        r11, r12, r21, r22 = r21, r22, r11, r12
    
    if (r21>=r11 and r22<= r12) or (r11>=r21 and r12<= r22):
        full_overlap += 1  

print(full_overlap)

# Part 2
any_overlap = 0
for l in lines:
    r1, r2 = l.strip().split(',')
    r11, r12 = [int(x) for x in r1.split('-')]
    r21, r22 = [int(x) for x in r2.split('-')]

    # So that r11 is always <= r21
    if r21<r11:
        r11, r12, r21, r22 = r21, r22, r11, r12    

    if ((r21>=r11) and (r21<=r12)) or ((r12>=r21) and (r12<=r22)):
        any_overlap += 1

print(any_overlap)
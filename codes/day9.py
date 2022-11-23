test = False

if test:
    input_file = '../inputs/day1_test'
else:
    input_file = '../inputs/day1_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

lines = [int(l.strip()) for l in lines]

# Part 1 
# Part 2
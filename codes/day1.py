test = False

if test:
    input_file = '../inputs/day1_test'
else:
    input_file = '../inputs/day1_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

# Part 1
sum_calories = []
current_sum = 0
for l in lines:
    if l.strip() != '':
        current_sum += int(l.strip())
    else:
        sum_calories.append(current_sum)
        current_sum = 0

sum_calories.append(current_sum)

print(max(sum_calories))

# Part 2
print(sum(sorted(sum_calories)[::-1][:3]))
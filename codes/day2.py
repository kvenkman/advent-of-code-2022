test = False

if test:
    input_file = '../inputs/day2_test'
else:
    input_file = '../inputs/day2_input'

with open(input_file, 'r') as f:
    lines = f.readlines()

# Rock (A) Paper (B) Scissors (C)
# Rock (X) Paper (Y) Scissors (Z)
strategy = {"A":["Y", "X"], "B":["Z", "Y"], "C":["X", "Z"]}
response_values = {"X":1, "Y":2, "Z":3}

# Part 1
score = 0
for l in lines:
    this_score = 0
    call, response = l.split()
    this_score += response_values[response]
    if response == strategy[call][0]:
        this_score += 6
    if response == strategy[call][1]:
        this_score += 3
    # print(this_score)
    score += this_score
print(score)

# Part 2
new_scoring = {"X":0, "Y":3, "Z":6}
call_values = {"A":1, "B":2, "C":3}

score = 0
for l in lines:
    this_score = 0
    call, response = l.split()
    this_score = new_scoring[response]
    call_score = call_values[call]
    
    # if lose:
    if this_score == 0:
        call_score = call_score - 1 if call_score > 1 else 3
    
    # if draw:
    if this_score == 3:
        pass
    
    # if win: 
    if this_score == 6:
        call_score = call_score + 1 if call_score < 3 else 1

    # print(this_score + call_score)

    score += (this_score+call_score)

print(score)
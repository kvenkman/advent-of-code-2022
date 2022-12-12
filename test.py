import os

input_file_path = './inputs'
codes_path='./codes'

for i in range(1, 26):
    ip_file = f"{input_file_path}/day{i}_input"
    ip_test_file = f"{input_file_path}/day{i}_test"
    op_file = f"{codes_path}/day{i}.py"
    template_file = "./template.py"

    with open(template_file) as f:
        lines = f.readlines()
    
    with open(ip_file, 'w') as f:
        pass

    with open(ip_test_file, 'w')  as f:
        pass

    with open(op_file, 'w') as f:
        for l in lines:
            f.write(l)


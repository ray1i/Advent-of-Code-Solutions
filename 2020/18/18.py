with open('18.txt', 'r') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

def next_bracket(s):
    c = 1
    for i in range(len(s)):
        if s[i] == '(':
            c += 1
        elif s[i] == ')':
            c -= 1
        if c == 0:
            return i + 1
#part one:
def evaluate(s):
    nums = []
    ops = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            nums.append(evaluate(s[i+1 : i+next_bracket(s[i+1:])]))
            i += next_bracket(s[i+1:])
        elif s[i] in '+*':
            ops.append(s[i])
            i += 2
        elif s[i] in '123456789':
            nums.append(int(s[i]))
            i += 2
        else:
            i += 1
    while len(ops) > 0:
        if ops[0] == '+':
            nums.insert(0, nums[0] + nums[1])
        elif ops[0] == '*':
            nums.insert(0, nums[0] * nums[1])
        ops.pop(0)
        nums.pop(1)
        nums.pop(1)
    return nums[0]
            

sum = 0
for equation in lines:
    sum += evaluate(equation)

print(f'part one: {sum}')

#part two:
def evaluate2(s):
    nums = []
    ops = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            nums.append(evaluate2(s[i+1 : i+next_bracket(s[i+1:])]))
            i += next_bracket(s[i+1:])
        elif s[i] in '+*':
            ops.append(s[i])
            i += 2
        elif s[i] in '123456789':
            nums.append(int(s[i]))
            i += 2
        else:
            i += 1
    while ops.count('+') > 0:
        i = 0
        while i < len(ops):
            if ops[i] == '+':
                nums.insert(i, nums[i] + nums[i + 1])
                ops.pop(i)
                nums.pop(i + 1)
                nums.pop(i + 1)
            i += 1
    while ops.count('*') > 0:
        if ops[0] == '*':
            nums.insert(0, nums[0] * nums[1])
        ops.pop(0)
        nums.pop(1)
        nums.pop(1)
    return nums[0]

sum2 = 0
for equation in lines:
    sum2 += evaluate2(equation)

print(f'part two: {sum2}')

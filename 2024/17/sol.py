from sys import stdin
from timeit import default_timer
from re import findall

type = 0
o_reg_a, o_reg_b, o_reg_c = 0, 0, 0
nums = []
for line in stdin:
    match type:
        case 0:
            o_reg_a = int(findall("-?\d+", line.strip())[0])
            type += 1
        case 1:
            o_reg_b = int(findall("-?\d+", line.strip())[0])
            type += 1
        case 2:
            o_reg_c = int(findall("-?\d+", line.strip())[0])
            type += 1
        case 3:
            type += 1
        case _:
            nums = [int(c) for c in findall("-?\d+", line.strip())]

# part one
start_time = default_timer()
ans = 0
reg_a, reg_b, reg_c = o_reg_a, o_reg_b, o_reg_c
i = 0
output = []
while i < len(nums):
    inst = nums[i]
    literal = nums[i + 1]
    combo = literal if 0 <= literal <= 3 else {4: reg_a, 5: reg_b, 6: reg_c}[literal]
    if inst == 0:
        reg_a = reg_a // (2**combo)
    elif inst == 1:
        reg_b = reg_b ^ literal
    elif inst == 2:
        reg_b = combo % 8
    elif inst == 3 and reg_a != 0:
        i = literal
        continue
    elif inst == 4:
        reg_b = reg_b ^ reg_c
    elif inst == 5:
        output.append(combo % 8)
    elif inst == 6:
        reg_b = reg_a // (2**combo)
    elif inst == 7:
        reg_c = reg_a // (2**combo)
    i += 2
ans = ",".join([str(n) for n in output])
end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
ans_list = [0]
while len(ans_list) <= len(nums):
    desired = nums[len(nums) - len(ans_list)]
    print("calculating", desired, len(nums) - len(ans_list))
    for test in range(ans_list[-1], 8):
        reg_a, reg_b, reg_c = ans * 8 + test, o_reg_b, o_reg_c
        i = 0
        output = -1
        while i < len(nums):
            inst = nums[i]
            literal = nums[i + 1]
            combo = (
                literal
                if 0 <= literal <= 3
                else {4: reg_a, 5: reg_b, 6: reg_c}[literal]
            )
            if inst == 0:
                reg_a = reg_a // (2**combo)
            elif inst == 1:
                reg_b = reg_b ^ literal
            elif inst == 2:
                reg_b = combo % 8
            elif inst == 3 and reg_a != 0:
                raise "what the fuck"
            elif inst == 4:
                reg_b = reg_b ^ reg_c
            elif inst == 5:
                output = combo % 8
                break
            elif inst == 6:
                reg_b = reg_a // (2**combo)
            elif inst == 7:
                reg_c = reg_a // (2**combo)
            i += 2
        if output == desired:
            ans = ans * 8 + test
            ans_list[-1] = test
            ans_list.append(0)
            break
    else:
        print("backtracking", ans_list)
        ans_list.pop()
        ans -= ans_list[-1]
        ans //= 8
        ans_list[-1] += 1

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

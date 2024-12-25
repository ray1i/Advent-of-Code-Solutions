from sys import stdin
from timeit import default_timer
from re import findall, match

vals = {}
ops = {}
args = {}
x_count = 0
y_count = 0
z_count = 0
inital_vals = True
for line in stdin:
    if line.strip() == "":
        inital_vals = False
        continue

    if inital_vals:
        wire = findall("(\w+):", line)[0]
        val = int(findall("(0|1)$", line.strip())[0])
        vals[wire] = val
        if wire[0] == "x":
            x_count += 1
        elif wire[0] == "y":
            y_count += 1
    else:
        m = match("(\w\w\w) (AND|OR|XOR) (\w\w\w) -> (\w\w\w)", line.strip())
        ops[m.group(4)] = m.group(2)
        args[m.group(4)] = (m.group(1), m.group(3))
        if m.group(4)[0] == "z":
            z_count += 1

# part one
start_time = default_timer()


def getVal(wire):
    if wire in vals:
        return vals[wire]
    a = getVal(args[wire][0])
    b = getVal(args[wire][1])
    ans = 0
    if ops[wire] == "AND":
        ans = a & b
    elif ops[wire] == "OR":
        ans = a | b
    elif ops[wire] == "XOR":
        ans = a ^ b
    # vals[wire] = ans
    return ans


ans = 0
digit = 0
for wire in sorted(args.keys()):
    if wire[0] == "z":
        ans |= getVal(wire) << digit
        digit += 1

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0

wrong = set()
for i in range(z_count):
    for k in vals.keys():
        vals[k] = 0

    for x in range(2):
        for y in range(2):
            if i <= 0:
                vals[f"x{str(i).zfill(2)}"] = x
                vals[f"y{str(i).zfill(2)}"] = y

                expected = (x + y) & 1
                actual = getVal(f"z{str(i).zfill(2)}")

                if expected != actual:
                    # print(
                    #     i,
                    #     x,
                    #     y,
                    #     f"expected: {expected}",
                    #     f"actual: {actual}",
                    # )
                    wrong.add(i)
            else:
                for x1 in range(2):
                    for y1 in range(2):
                        vals[f"x{str(i-1).zfill(2)}"] = x1
                        vals[f"y{str(i-1).zfill(2)}"] = y1
                        vals[f"x{str(i).zfill(2)}"] = x
                        vals[f"y{str(i).zfill(2)}"] = y

                        expected = (((x1 + y1) >> 1) + (x + y)) & 1
                        actual = getVal(f"z{str(i).zfill(2)}")

                        if expected != actual:
                            # print(
                            #     i,
                            #     x,
                            #     y,
                            #     x1,
                            #     y1,
                            #     f"expected: {expected}",
                            #     f"actual: {actual}",
                            # )
                            wrong.add(i)
print(wrong)

sums = {}
carry = {}
for k in ops.keys():
    if ops[k] == "AND" and "".join(sorted([args[k][0][0], args[k][1][0]])) == "xy":
        # carry[f"z{args[k][0][1:]}"] = k
        carry[k] = f"z{args[k][0][1:]}"
    elif ops[k] == "XOR" and "".join(sorted([args[k][0][0], args[k][1][0]])) == "xy":
        # sums[f"z{args[k][0][1:]}"] = k
        sums[k] = f"z{args[k][0][1:]}"

print(sorted(sums.items()))
print(sorted(carry.items()))

intermediate_carry = {}  # e.g. c00 AND s01
for k in ops.keys():
    if ops[k] == "AND" and "".join(sorted([args[k][0][0], args[k][1][0]])) != "xy":
        if args[k][0] in carry and args[k][1] in sums:
            intermediate_carry[k] = f"z{sums[args[k][1]][1:]}"
        elif args[k][0] in sums and args[k][1] in carry:
            intermediate_carry[k] = f"z{sums[args[k][0]][1:]}"
        else:
            print(f"bad inter: {args[k]}")
print(sorted(intermediate_carry.items()))

for k in ops.keys():
    if ops[k] == "OR":
        if args[k][0] in carry:
            pass
        elif args[k][1] in carry:
            pass
        else:
            print(f"bad OR: {args[k]}")

# print(carry)
# print(sums)
# print(carry["z00"], carry["z01"])


# for guh in ["z00", "z01", "z02", "z03", "z04"]:
for i in range(z_count):
    guh = f"z{str(i).zfill(2)}"

    if guh == "z00":
        sums

    q = [guh]
    while len(q) > 0:
        w = q.pop()
        if w in ops:
            # print(w, ops[w], args[w])
            if ops[w] == "AND":
                carry[ops[w]] = guh
            else:
                q.append(args[w][0])
                q.append(args[w][1])
    # print("-=-=-")

# Hand to hand solve :(


end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

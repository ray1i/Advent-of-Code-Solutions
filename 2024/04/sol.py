from sys import stdin
from timeit import default_timer

lines = []
for line in stdin:
    lines.append(line.strip())


# part one
def containsXMAS(x, y):
    if lines[x][y] != "X":
        return 0

    s = 0
    if x - 3 >= 0:  # north
        s += 1 if lines[x - 1][y] + lines[x - 2][y] + lines[x - 3][y] == "MAS" else 0
    if x - 3 >= 0 and y + 3 < len(lines[0]):  # northeast
        s += (
            1
            if lines[x - 1][y + 1] + lines[x - 2][y + 2] + lines[x - 3][y + 3] == "MAS"
            else 0
        )
    if y + 3 < len(lines[0]):  # east
        s += 1 if lines[x][y + 1] + lines[x][y + 2] + lines[x][y + 3] == "MAS" else 0
    if x + 3 < len(lines) and y + 3 < len(lines[0]):  # southeast
        s += (
            1
            if lines[x + 1][y + 1] + lines[x + 2][y + 2] + lines[x + 3][y + 3] == "MAS"
            else 0
        )
    if x + 3 < len(lines[0]):  # south
        s += 1 if lines[x + 1][y] + lines[x + 2][y] + lines[x + 3][y] == "MAS" else 0
    if x + 3 < len(lines) and y - 3 >= 0:  # southwest
        s += (
            1
            if lines[x + 1][y - 1] + lines[x + 2][y - 2] + lines[x + 3][y - 3] == "MAS"
            else 0
        )
    if y - 3 >= 0:  # west
        s += 1 if lines[x][y - 1] + lines[x][y - 2] + lines[x][y - 3] == "MAS" else 0
    if x - 3 >= 0 and y - 3 >= 0:  # northwest
        s += (
            1
            if lines[x - 1][y - 1] + lines[x - 2][y - 2] + lines[x - 3][y - 3] == "MAS"
            else 0
        )

    return s


start_time = default_timer()
ans = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        ans += containsXMAS(i, j)

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")


# part two
def containsX_MAS(x, y):
    if lines[x][y] != "M":
        return 0

    s = 0

    # S.S
    # .A.
    # M.M
    # ^
    if x - 2 >= 0 and y + 2 < len(lines[0]):  # north
        s += (
            1
            if lines[x][y + 2]
            + lines[x - 1][y + 1]
            + lines[x - 2][y]
            + lines[x - 2][y + 2]
            == "MASS"
            else 0
        )
    # v
    # M.S
    # .A.
    # M.S
    if x + 2 < len(lines) and y + 2 < len(lines[0]):  # east
        s += (
            1
            if lines[x + 2][y]
            + lines[x + 1][y + 1]
            + lines[x][y + 2]
            + lines[x + 2][y + 2]
            == "MASS"
            else 0
        )
    #   v
    # M.M
    # .A.
    # X.S
    if x + 2 < len(lines) and y - 2 >= 0:  # south
        s += (
            1
            if lines[x][y - 2]
            + lines[x + 1][y - 1]
            + lines[x + 2][y]
            + lines[x + 2][y - 2]
            == "MASS"
            else 0
        )
    # S.M
    # .A.
    # S.M <
    if x - 2 >= 0 and y - 2 >= 0:  # west
        s += (
            1
            if lines[x - 2][y]
            + lines[x - 1][y - 1]
            + lines[x][y - 2]
            + lines[x - 2][y - 2]
            == "MASS"
            else 0
        )

    return s


ans = 0
start_time = default_timer()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        ans += containsX_MAS(i, j)

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

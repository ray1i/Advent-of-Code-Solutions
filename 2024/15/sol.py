from sys import stdin
from timeit import default_timer

arrow_to_move = {"^": 0, ">": 1, "v": 2, "<": 3}
move_to_d = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

o_grid = []
moves = []
ox, oy = -1, -1
getting_grid = True
for line in stdin:
    if line.strip() == "":
        getting_grid = False
    elif getting_grid:
        o_grid.append([c for c in line.strip()])
        if "@" in line:
            ox = line.find("@")
            oy = len(o_grid) - 1
            o_grid[oy][ox] = "."
    else:
        moves += [arrow_to_move[c] for c in line.strip()]

m = len(o_grid)
n = len(o_grid[0])

# part one
start_time = default_timer()
ans = 0
grid = [line.copy() for line in o_grid]
x, y = ox, oy
for move in moves:
    mx = x + move_to_d[move][0]
    my = y + move_to_d[move][1]
    if grid[my][mx] == ".":
        x, y = mx, my
    elif grid[my][mx] == "O":
        i = 2
        while grid[y + move_to_d[move][1] * i][x + move_to_d[move][0] * i] == "O":
            i += 1
        if grid[y + move_to_d[move][1] * i][x + move_to_d[move][0] * i] == ".":
            grid[y + move_to_d[move][1] * i][x + move_to_d[move][0] * i] = "O"
            grid[my][mx] = "."
            x, y = mx, my

for i in range(m):
    for j in range(n):
        if grid[i][j] == "O":
            ans += i * 100 + j

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()

ans = 0
grid = [sum([[c] * 2 if c != "O" else ["[", "]"] for c in line], []) for line in o_grid]
x, y = ox * 2, oy
for move in moves:
    mx = x + move_to_d[move][0]
    my = y + move_to_d[move][1]
    if grid[my][mx] == ".":
        x, y = mx, my
    elif grid[my][mx] in "[]" and move in [1, 3]:
        i = 2
        while grid[y + move_to_d[move][1] * i][x + move_to_d[move][0] * i] in "[]":
            i += 1
        if grid[y + move_to_d[move][1] * i][x + move_to_d[move][0] * i] == ".":
            c = "]" if move == 3 else "["
            for j in range(2, i + 1):
                grid[y + move_to_d[move][1] * j][x + move_to_d[move][0] * j] = c
                c = "[" if c == "]" else "]"
            grid[my][mx] = "."
            x, y = mx, my
    elif grid[my][mx] in "[]" and move in [0, 2]:
        rows = [[(mx, my) if grid[my][mx] == "[" else (mx - 1, my)]]
        while len(rows[-1]) > 0 and not any(
            [grid[ty][tx] == "#" for tx, ty in rows[-1]]
        ):
            new_row = []
            for bx, by in rows[-1]:
                if grid[by + move_to_d[move][1]][bx + move_to_d[move][0]] in "[#":
                    new_row.append((bx + move_to_d[move][0], by + move_to_d[move][1]))
                elif (
                    grid[by + move_to_d[move][1]][bx + move_to_d[move][0]] == "]"
                    and (bx + move_to_d[move][0] - 1, by + move_to_d[move][1])
                    not in new_row
                ):
                    new_row.append(
                        (bx + move_to_d[move][0] - 1, by + move_to_d[move][1])
                    )

                if grid[by + move_to_d[move][1]][bx + move_to_d[move][0] + 1] in "[#":
                    new_row.append(
                        (bx + move_to_d[move][0] + 1, by + move_to_d[move][1])
                    )

            rows.append(new_row)
        if any([grid[ty][tx] == "#" for tx, ty in rows[-1]]):
            continue

        walls = sum(rows, [])
        for wx, wy in walls:
            grid[wy][wx] = "."
            grid[wy][wx + 1] = "."
        for wx, wy in walls:
            grid[wy + move_to_d[move][1]][wx + move_to_d[move][0]] = "["
            grid[wy + move_to_d[move][1]][wx + move_to_d[move][0] + 1] = "]"
        x, y = mx, my

for i in range(m):
    for j in range(n * 2):
        if grid[i][j] == "[":
            ans += i * 100 + j

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

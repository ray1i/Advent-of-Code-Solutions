from sys import stdin
from timeit import default_timer
from functools import lru_cache
from collections import deque
from re import findall

nums = []
for line in stdin:
    nums.append(line.strip())

numeric_grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
numeric_pos = {}
for i, row in enumerate(numeric_grid):
    for j, c in enumerate(row):
        numeric_pos[c] = (j, i)
arrow_grid = [["", "^", "A"], ["<", "v", ">"]]
arrow_pos = {}
for i, row in enumerate(arrow_grid):
    for j, c in enumerate(row):
        arrow_pos[c] = (j, i)


@lru_cache(None)
def getAllSequences(isNums, start, end):
    grid = numeric_grid if isNums else arrow_grid
    pos = numeric_pos if isNums else arrow_pos

    m = len(grid)
    n = len(grid[0])

    ox, oy = pos[start]
    q = deque([(ox, oy, "", [start])])  # moves list, chars lits
    res = []
    while len(q) > 0:
        x, y, prev_move, prev_char = q.popleft()
        for dx, dy, move in [(-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")]:
            nx, ny = x + dx, y + dy
            if (
                not (0 <= nx < n and 0 <= ny < m)
                or not grid[ny][nx]
                or grid[ny][nx] in prev_char
            ):
                continue
            elif grid[ny][nx] == end:
                res.append(prev_move + move)
            else:
                q.append((nx, ny, prev_move + move, prev_char + [grid[y][x]]))

    return res


@lru_cache
def getShortestSequenceLength(
    isNums,
    levels,
    sequence,
):
    res = 0
    prev = "A"
    for c in sequence:
        curr_shortest = 0
        for s in getAllSequences(isNums, prev, c):
            shortest = (
                len(s)
                if levels <= 1
                else getShortestSequenceLength(False, levels - 1, s + "A")
            )
            if shortest < curr_shortest or not curr_shortest:
                curr_shortest = shortest
        prev = c
        res += (
            curr_shortest + 1
            if levels <= 1
            else ((curr_shortest if curr_shortest else 1))
        )
    return res


# part one
start_time = default_timer()
ans = 0

for code in nums:
    path = getShortestSequenceLength(True, 3, code)
    complexity = int(findall("\d+", code)[0]) * path
    ans += complexity

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
for code in nums:
    path = getShortestSequenceLength(True, 26, code)
    complexity = int(findall("\d+", code)[0]) * path
    ans += complexity

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

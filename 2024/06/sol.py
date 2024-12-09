from sys import stdin
from timeit import default_timer

obstacle = []
ogx = -1
ogy = -1
for line in stdin:
    r = [False]
    for i, c in enumerate(line.strip()):
        if c == "^":
            ogx = i + 1
            ogy = len(obstacle) + 1
            r.append(False)
        elif c == "#":
            r.append(True)
        else:
            r.append(False)
    r.append(False)
    obstacle.append(r)

obstacle.insert(0, [False] * len(obstacle[0]))
obstacle.append([False] * len(obstacle[0]))

n = len(obstacle[0])
m = len(obstacle)

dirs = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}

# part one
start_time = default_timer()
ans = 0
gx = ogx
gy = ogy
visited = [[False] * n for _ in range(m)]
d = 0  # n = 0, e = 1, s = 2, w = 3
while 0 < gx < n - 1 and 0 < gy < m - 1:
    if not visited[gy][gx]:
        ans += 1
        visited[gy][gx] = True

    while obstacle[gy + dirs[d][0]][gx + dirs[d][1]]:
        d = (d + 1) % 4

    gx += dirs[d][1]
    gy += dirs[d][0]

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")


# part two
start_time = default_timer()
ans = 0
ans_list = set()
gx = ogx
gy = ogy
d = 0  # n = 0, e = 1, s = 2, w = 3
visited = [
    [
        [
            False,
            False,
            False,
            False,
        ]
        for __ in range(n)
    ]
    for _ in range(m)
]
while 0 < gx < n - 1 and 0 < gy < m - 1:
    visited[gy][gx][d] = True

    while obstacle[gy + dirs[d][0]][gx + dirs[d][1]]:
        d = (d + 1) % 4

    if (
        0 < gx + dirs[d][1] < n - 1
        and 0 < gy + dirs[d][0] < m - 1
        and (gx + dirs[d][1], gy + dirs[d][0]) not in ans_list
        and not visited[gy + dirs[d][0]][gx + dirs[d][1]][0]
        and not visited[gy + dirs[d][0]][gx + dirs[d][1]][1]
        and not visited[gy + dirs[d][0]][gx + dirs[d][1]][2]
        and not visited[gy + dirs[d][0]][gx + dirs[d][1]][3]
    ):
        obstacle[gy + dirs[d][0]][gx + dirs[d][1]] = True
        fake_x = gx
        fake_y = gy
        fake_d = (d + 1) % 4
        moves = []
        while 0 < fake_x < n - 1 and 0 < fake_y < m - 1:
            if visited[fake_y][fake_x][fake_d]:
                ans_list.add((gx + dirs[d][1], gy + dirs[d][0]))
                ans += 1
                break

            moves.append((fake_x, fake_y, fake_d))
            visited[fake_y][fake_x][fake_d] = True

            while obstacle[fake_y + dirs[fake_d][0]][fake_x + dirs[fake_d][1]]:
                fake_d = (fake_d + 1) % 4

            fake_x += dirs[fake_d][1]
            fake_y += dirs[fake_d][0]

        for move in moves:
            visited[move[1]][move[0]][move[2]] = False
        obstacle[gy + dirs[d][0]][gx + dirs[d][1]] = False

    gx += dirs[d][1]
    gy += dirs[d][0]

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

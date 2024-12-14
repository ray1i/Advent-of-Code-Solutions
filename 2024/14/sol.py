from sys import stdin
from timeit import default_timer
from re import findall

robots = []
for line in stdin:
    robots.append(tuple([int(n) for n in findall("([-]?\d+)", line)]))

WIDTH = 101
HEIGHT = 103
# WIDTH = 11
# HEIGHT = 7

# part one
start_time = default_timer()
SECONDS = 100
quadrants = [0, 0, 0, 0]
ans = 0
for x, y, vx, vy in robots:
    x_final = (x + vx * SECONDS) % WIDTH
    y_final = (y + vy * SECONDS) % HEIGHT

    if 0 <= x_final < WIDTH // 2 and 0 <= y_final < HEIGHT // 2:
        quadrants[0] += 1
    elif WIDTH // 2 < x_final <= WIDTH and 0 <= y_final < HEIGHT // 2:
        quadrants[1] += 1
    elif 0 <= x_final < WIDTH // 2 and HEIGHT // 2 < y_final <= HEIGHT:
        quadrants[2] += 1
    elif WIDTH // 2 < x_final <= WIDTH and HEIGHT // 2 < y_final <= HEIGHT:
        quadrants[3] += 1

ans = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
i = 1
while True:
    grid = [["."] * WIDTH for _ in range(HEIGHT)]

    for x, y, vx, vy in robots:
        x_final = (x + vx * i) % WIDTH
        y_final = (y + vy * i) % HEIGHT
        grid[y_final][x_final] = "#"

    s = "\n".join(["".join(g) for g in grid])
    if "###########" in s:
        # print(s)
        # print("---", i, "---")
        ans = i
        break

    i += 1

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

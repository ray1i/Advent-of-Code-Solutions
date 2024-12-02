from sys import stdin

reports = []
for line in stdin:
    nums = [int(n.strip()) for n in line.strip().split()]
    reports.append(nums)

# part one
ans = 0
for r in reports:
    isInc = r[0] < r[1]
    ans += 1
    for i in range(len(r) - 1):
        if (isInc and r[i] > r[i + 1]) or (not isInc and r[i] < r[i + 1]):
            ans -= 1
            break
        if not 1 <= abs(r[i] - r[i + 1]) <= 3:
            ans -= 1
            break

print("part 1:", ans)


# part two
def isSafe(levels):
    isInc = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        if (
            (isInc and levels[i] > levels[i + 1])
            or (not isInc and levels[i] < levels[i + 1])
            or (not 1 <= abs(levels[i] - levels[i + 1]) <= 3)
        ):
            return False
    return True


ans = 0
for r in reports:
    if isSafe(r):
        ans += 1
    else:
        for i in range(len(r)):
            if isSafe(r[:i] + r[i + 1 :]):
                ans += 1
                break

print("part 2:", ans)

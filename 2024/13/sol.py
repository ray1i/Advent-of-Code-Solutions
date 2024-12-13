from sys import stdin
from timeit import default_timer
from re import findall
from math import gcd

nums = []
for line in stdin:
    # Button A
    a = tuple([int(n) for n in findall("[X|Y]\+(\d+)", line)])
    line = stdin.readline()

    # Button B
    b = tuple([int(n) for n in findall("[X|Y]\+(\d+)", line)])
    line = stdin.readline()

    # Prize
    prize = tuple([int(n) for n in findall("[X|Y]=(\d+)", line)])
    line = stdin.readline()

    nums.append((a, b, prize))


# part one
def solutions(a: int, b: int, c: int) -> tuple[int, int]:
    # extended Euclidean algorithm
    if a > b:
        ri, rj = a, b
    else:
        ri, rj = b, a
    si, sj = 1, 0
    ti, tj = 0, 1

    while rj != 0:
        q = ri // rj
        ri, rj = rj, ri - q * rj
        si, sj = sj, si - q * sj
        ti, tj = tj, ti - q * tj

    d = gcd(a, b)
    ar = a // d if a > b else b // d
    br = b // d if a > b else a // d
    s = si * (c // d)
    t = ti * (c // d)

    res = []
    if s < t:
        while s <= 100:
            if 0 <= s <= 100 and 0 <= t <= 100:
                if a > b:
                    res.append((s, t))
                else:
                    res.append((t, s))
            s += br
            t -= ar
        if a > b:
            res.reverse()
    else:
        while t <= 100:
            if 0 <= s <= 100 and 0 <= t <= 100:
                if a > b:
                    res.append((s, t))
                else:
                    res.append((t, s))
            s -= br
            t += ar
        if a <= b:
            res.reverse()
    return res


start_time = default_timer()
ans = 0
for (ax, ay), (bx, by), (px, py) in nums:
    # Diophantine equation type shit
    # find solutions for s*ax + t*bx = px and u*ay + v*by = py
    # and get the matching pairs, where s == u and t == v
    # and get one where t is lowest.

    dx = gcd(ax, bx)
    dy = gcd(ay, by)

    if px % dx != 0 or py % dy != 0:
        # no solution
        continue

    xsols = solutions(ax, bx, px)
    ysols = solutions(ay, by, py)

    ysols_set = set(ysols)
    for pair in xsols:
        if pair in ysols_set:
            ans += 3 * pair[0] + pair[1]
            break

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")


# part two
DIFF = 10000000000000


def solutions_nomax(a: int, b: int, c: int) -> tuple[int, int]:
    # extended Euclidean algorithm
    if a > b:
        ri, rj = a, b
    else:
        ri, rj = b, a
    si, sj = 1, 0
    ti, tj = 0, 1

    while rj != 0:
        q = ri // rj
        ri, rj = rj, ri - q * rj
        si, sj = sj, si - q * sj
        ti, tj = tj, ti - q * tj

    d = gcd(a, b)
    ar = a // d if a > b else b // d
    br = b // d if a > b else a // d
    s = si * (c // d)
    t = ti * (c // d)

    if s < t:
        k = abs(s) // br + 1
        s += br * k
        t -= ar * k
        if a > b:
            return (s, t)
        else:
            return (t, s)
    else:
        k = abs(t) // ar + 1
        s -= br * k
        t += ar * k
        if a > b:
            return (s, t)
        else:
            return (t, s)


start_time = default_timer()
ans = 0
for (ax, ay), (bx, by), (px, py) in nums:
    dx = gcd(ax, bx)
    dy = gcd(ay, by)

    if (px + DIFF) % dx != 0 or (py + DIFF) % dy != 0:
        # no solution
        continue

    s, t = solutions_nomax(ax, bx, px + DIFF)
    u, v = solutions_nomax(ay, by, py + DIFF)

    # magic formulas
    axr = ax // dx
    bxr = bx // dx
    ayr = ay // dy
    byr = by // dy

    # what the fuck
    k = (u * ayr + byr * (v - t) - s * ayr) // (bxr * ayr - axr * byr)
    k_prime = (v - t + k * axr) // ayr

    if (
        ax * (s + k * bxr) + bx * (t - k * axr) == px + DIFF
        and ay * (s + k * bxr) + by * (t - k * axr) == py + DIFF
        and s + k * bxr >= 0
        and t - k * axr >= 0
    ):
        ans += abs(s + k * bxr) * 3 + abs(t - k * axr)

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

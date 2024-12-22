from sys import stdin
from timeit import default_timer
from collections import defaultdict

nums = []
for line in stdin:
    nums.append(int(line.strip()))

# part one
start_time = default_timer()
ans = 0
for n in nums:
    for i in range(2000):
        n = (n ^ (n * 64)) % 16777216
        n = (n ^ (n // 32)) % 16777216
        n = (n ^ (n * 2048)) % 16777216
    ans += n

end_time = default_timer()
print(f"part 1: {ans} (took {(end_time - start_time) * 1000} ms)")

# part two
start_time = default_timer()
ans = 0
# 16777216 = 2 ** 24
sums = defaultdict(int)
for n in nums:
    diffs = ()
    seen = set()
    for i in range(2000):
        m = n
        m ^= m << 6
        m ^= (m >> 5) & 0b1111111111111111111
        m ^= m << 11
        m &= 0b111111111111111111111111

        diffs = (
            diffs + (m % 10 - n % 10,)
            if len(diffs) < 4
            else (diffs[1], diffs[2], diffs[3], m % 10 - n % 10)
        )
        if diffs not in seen:
            sums[diffs] += m % 10
            ans = max(ans, sums[diffs])
            seen.add(diffs)
        n = m

# X X X X X X X X X X X X X X X X X X X X X X X X X X
# X X X X X X X X X X X X X X X X X X X X 0 0 0 0 0 0
# 0 X X X X X X X X X X X X X X X X X X X X 0 0 0 0 0
# X X X X X X X X X X X X X X 0 0 0 0 0 0 0 0 0 0 0 0
# A B C D E F G H I J K L M N O P Q R S T U V W X
# G H I J K L M N O P Q R S T U V W X 0 0 0 0 0 0
# 0 G H I J K L M N O P Q R S T U V W X 0 0 0 0 0
# L M N O P Q R S T U V W X 0 0 0 0 0 0 0 0 0 0 0

end_time = default_timer()
print(f"part 2: {ans} (took {(end_time - start_time) * 1000} ms)")

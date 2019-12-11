def fuel(n):
    return ((n//3)-2)

s = 0

#part 1:
'''while True:
    n = int(input())
    s = s + fuel(n)
    if n == 121214:
        break

print(s)'''

while True:
    n = int(input())
    m = fuel(n)
    s += m
    m = fuel(m)
    while m > 0:
        s += m
        m = fuel(m)

    if n == 121214:
        break


print(s)

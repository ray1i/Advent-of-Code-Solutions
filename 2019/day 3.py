# Part 1:
'''
wired1 = [s for s in input().split(',')]
wired2 = [s for s in input().split(',')]

w1 = set()
w2 = set()

def makelist(d, w):
    x = 0
    y = 0
    for i in d:
        if i[0] == 'R':
            for j in range(int(i[1:])):
                w.add((x + j, y))
            x += int(i[1:])
        elif i[0] == 'L':
            for j in range(int(i[1:])):
                w.add((x - j, y))
            x -= int(i[1:])
        elif i[0] == 'U':
            for j in range(int(i[1:])):
                w.add((x, y + j))
            y += int(i[1:])
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                w.add((x, y - j))
            y -= int(i[1:])

makelist(wired1, w1)
makelist(wired2, w2)
w1.remove((0, 0))
w2.remove((0, 0))

intersect = set(w1.intersection(w2))

minimum = 999999999999999

for i in intersect:
    if abs(i[0]) + abs(i[1]) < minimum:
        #print('yes', i)
        minimum = abs(i[0]) + abs(i[1])

print(minimum)
'''
#Part 2:

wired1 = [s for s in input().split(',')]
wired2 = [s for s in input().split(',')]

w1 = {}
w2 = {}

def zz(z):
    z += 1
    return z

def makelist(d, w):
    x = 0
    y = 0
    z = -1
    for i in d:
        if i[0] == 'R':
            for j in range(int(i[1:])):
                z += 1
                if (x + j, y) in w:
                    pass
                else:
                    w[(x + j, y)] = z
            x += int(i[1:])
        elif i[0] == 'L':
            for j in range(int(i[1:])):
                z += 1
                if (x - j, y) in w:
                    pass
                else:
                    w[(x - j, y)] = zz(z)
            x -= int(i[1:])
        elif i[0] == 'U':
            for j in range(int(i[1:])):
                z += 1
                if (x, y + j) in w:
                    pass
                else:
                    w[(x, y + j)] = zz(z)
            y += int(i[1:])
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                z += 1
                if (x, y -j) in w:
                    pass
                else:
                    w[(x, y - j)] = zz(z)
            y -= int(i[1:])

makelist(wired1, w1)
makelist(wired2, w2)
w1.pop((0, 0))
w2.pop((0, 0))

w1values = set(w1.keys())
w2values = set(w2.keys())

intersect = set(w1values.intersection(w2values))

minimum = 999999999999999

for i in intersect:
    if w1[i] + w2[i] < minimum:
        print('yes', i)
        minimum = w1[i] + w2[i]

print(minimum - 1) #i don't know why i need to -1 but i just do.

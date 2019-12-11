#this is the most scuffed code i've ever written but it works and i'm happy

import copy

spacemap = []
inp = ''
endin = '..#...#.###...##....##.#.#.#....#.#.'
while inp != endin:
    inp = input()
    row = []
    for i in range(len(inp)):
        row.append(inp[i])
    spacemap.append(row)

w = len(spacemap[0])
h = len(spacemap)

#for i in range(h):
    #print(spacemap[i])

dists = [[0 for s in range(w)] for s in range(h)]

def gcd(a,b):
    if a == b == 0:
        return 1
    elif a == 0:
        return b
    elif b == 0:
        return a 
    if a > b: 
        small = b 
    else:
        small = a 
    for i in range(1, small+1): 
        if((a % i == 0) and (b % i == 0)): 
            d = i 
    return d

#print(gcd(0,0))'


#part 1:
'''
def detect(x, y):
    m = copy.deepcopy(spacemap)
    m[y][x] = 'O'
    #if x == 7 and y == 9:
    #    for i in range(h):
    #        print(m[i])

    for rise in range(-y, h - y + 1):
        for run in range(-x, h - x + 1):
            g = gcd(abs(rise), abs(run))
            lowrise = int(rise/g)
            lowrun = int(run/g)
            #if x == 7 and y == 9:
            #    print(rise, run, g, lowrise, lowrun)
            for n in range(1, h):
                if y + lowrise * n >= 0 and x + lowrun * n >= 0:
                    try:
                        if m[y + lowrise * n][x + lowrun * n] == 'X':
                            break
                        elif m[y + lowrise * n][x + lowrun * n] == '#':
                            #if x == 7 and y == 9:
                            #    print(lowrise, lowrun, n)
                            #if y + lowrise * n == 7 and x + lowrun * n == 9:
                            #    print('yes')
                            #print(y + lowrise * n, x + lowrun * n)
                            #if x == 7 and y == 9:
                            #    for i in range(h):
                            #        print(m[i])
                            #    print(y + lowrise * n, x + lowrun * n, lowrise, lowrun, n)#
                            dists[y][x] += 1
                            m[y + lowrise * n][x + lowrun * n] = 'X'
                            break
                    except IndexError:
                        break
    #for i in range(h):
    #    print(m[i])
    #print(x, y)

maxdist = 0
maxcoord = []
for y in range(h):
    for x in range(w):
        #print(spacemap[y][x])
        if spacemap[y][x] == '#':
            detect(x, y)
            #print(x, y)
            if dists[y][x] > maxdist:
                maxdist = dists[y][x]
                maxcoord = [x, y]

#for i in range(h):
    #print(dists[i])


print(maxdist, maxcoord)
'''



#part two:


#x = maxcoord[0]
#y = maxcoord[1]
x = 25
y = 31
anglesq1 = {}
anglesq2 = {}
anglesq3 = {}
anglesq4 = {}

def detectangles(x, y):
    m = copy.deepcopy(spacemap)
    m[y][x] = 'O'

    for rise in range(-y, h - y + 1):
        for run in range(-x, h - x + 1):
            g = gcd(abs(rise), abs(run))
            lowrise = int(rise/g)
            lowrun = int(run/g)
            for n in range(1, h):
                if y + lowrise * n >= 0 and x + lowrun * n >= 0:
                    try:
                        if m[y + lowrise * n][x + lowrun * n] == 'X':
                            break
                        elif m[y + lowrise * n][x + lowrun * n] == '#':
                            if lowrise < 0 and lowrun > 0:
                                anglesq1[lowrise/lowrun] = (lowrise, lowrun)
                            elif lowrise > 0 and lowrun > 0:
                                anglesq4[lowrise/lowrun] = (lowrise, lowrun)
                            elif lowrise > 0 and lowrun < 0:
                                anglesq3[lowrise/lowrun] = (lowrise, lowrun)
                            elif lowrise < 0 and lowrun < 0:
                                anglesq2[lowrise/lowrun] = (lowrise, lowrun)
                            dists[y][x] += 1
                            m[y + lowrise * n][x + lowrun * n] = 'X'
                            break
                    except IndexError:
                        break

detectangles(x, y)
'''print(anglesq1)
print(anglesq4)
print(anglesq3)
print(anglesq2)'''

q1 = sorted(anglesq1.keys())
q4 = sorted(anglesq4.keys())
q3 = sorted(anglesq3.keys())
q2 = sorted(anglesq2.keys())

m = copy.deepcopy(spacemap)
m[y][x] = 'O'

astcounter = 0

def rotate(m, x, y, astcounter):
    #straight up
    for n in range(1, h):
        if y - n >= 0:
            try:
                if m[y - n][x] == '#':
                    astcounter += 1
                    print(astcounter, ':', y - n, x)
                    m[y - n][x] == '.'
                    break
            except IndexError:
                break

    #q1
    for i in q1:
        rise = anglesq1[i][0]
        run = anglesq1[i][1]
        for n in range(1, h):
            if y + rise * n >= 0 and x + run * n >= 0:
                try:
                    if m[y + rise * n][x + run * n] == '#':
                        astcounter += 1
                        print(astcounter, ':', y + rise * n, x + run * n)
                        m[y + rise * n][x + run * n] == '.'
                        break
                except IndexError:
                    break

    #straight left
    for n in range(1, h):
        if x + n >= 0:
            try:
                if m[y][x + n] == '#':
                    astcounter += 1
                    print(astcounter, ':', y, x + n)
                    m[y][x + n] == '.'
                    break
            except IndexError:
                break

    #q4
    for i in q4:
        rise = anglesq4[i][0]
        run = anglesq4[i][1]
        for n in range(1, h):
            if y + rise * n >= 0 and x + run * n >= 0:
                try:
                    if m[y + rise * n][x + run * n] == '#':
                        astcounter += 1
                        print(astcounter, ':', y + rise * n, x + run * n)
                        m[y + rise * n][x + run * n] == '.'
                        break
                except IndexError:
                    break

    #straight down
    for n in range(1, h):
        if y + n >= 0:
            try:
                if m[y + n][x] == '#':
                    astcounter += 1
                    print(astcounter, ':', y + n, x)
                    m[y + n][x] == '.'
                    break
            except IndexError:
                break
    
    #q3
    for i in q3:
        rise = anglesq3[i][0]
        run = anglesq3[i][1]
        for n in range(1, h):
            if y + rise * n >= 0 and x + run * n >= 0:
                try:
                    if m[y + rise * n][x + run * n] == '#':
                        astcounter += 1
                        print(astcounter, ':', y + rise * n, x + run * n)
                        m[y + rise * n][x + run * n] == '.'
                        break
                except IndexError:
                    break

    #straight left
    for n in range(1, h):
        if x - n >= 0:
            try:
                if m[y][x - n] == '#':
                    astcounter += 1
                    print(astcounter, ':', y, x - n)
                    m[y][x - n] == '.'
                    break
            except IndexError:
                break

    #q2
    for i in q2:
        rise = anglesq2[i][0]
        run = anglesq2[i][1]
        for n in range(1, h):
            if y + rise * n >= 0 and x + run * n >= 0:
                try:
                    if m[y + rise * n][x + run * n] == '#':
                        astcounter += 1
                        print(astcounter, ':', y + rise * n, x + run * n)
                        m[y + rise * n][x + run * n] == '.'
                        break
                except IndexError:
                    break

rotate(m, x, y, astcounter)

#while True:
    #print('rotating')
    #rotate(m, x, y)

original = [int(s) for s in input().split(',')]
o = original.copy()
for i in range(1000000):
    o.append(0)

input = 0
relbase = 0
outputs = []

go = True

def assignpara(oc, ocpos, opos, c):
    if oc[ocpos] == 0:
        if c:
            return o[n + opos]
        else:
            return o[o[n + opos]]
    elif oc[ocpos] == 1:
        return o[n + opos]
    elif oc[ocpos] == 2:
        if c:
            return relbase + o[n + opos]
        else:
            return o[relbase + o[n + opos]]
    else:
        print('assignpara fail')


inputindex = 0

def parse(n):
    global relbase
    oc = str(o[n])
    if len(oc) < 5:
        oc = (5-len(oc))*'0' + oc
    oc = [int(s) for s in oc]
    a = assignpara(oc, -3, 1, False)

    if oc[-1] == 1 or oc[-1] == 2:
        b = assignpara(oc, -4, 2, False)
        c = assignpara(oc, -5, 3, True)
        if oc[-1] == 1:
            o[c] = a + b 
        elif oc[-1] == 2:
            o[c] = a * b
        return n + 4

    elif oc[-1] == 3:
        a = assignpara(oc, -3, 1, True) #special case
        global inputindex
        o[a] = input[inputindex]
        inputindex += 1
        return n + 2

    elif oc[-1] == 4:
        outputs.append(a)
        return n + 2
    
    elif oc[-1] == 5 or oc[-1] == 6:
        b = assignpara(oc, -4, 2, False)
        if oc[-1] == 5:
            if a != 0:
                return b
        elif oc[-1] == 6:
            if a == 0:
                return b
        return n + 3

    elif oc[-1] == 7:
        b = assignpara(oc, -4, 2, False)
        c = assignpara(oc, -5, 3, True)
        if a < b:
            o[c] = 1
        else:
            o[c] = 0
        return n + 4
    
    elif oc[-1] == 8:
        b = assignpara(oc, -4, 2, False)
        c = assignpara(oc, -5, 3, True)
        if a == b:
            o[c] = 1
        else:
            o[c] = 0
        return n + 4

    elif oc[-1] == 9 and oc[-2] == 0:
        relbase += a
        return n + 2

    elif oc[-1] == 9 and oc[-2] == 9:
        global go
        go = False
        return n + 1
        
    else:
        print('fail')

n = 0
while go:
    n = parse(n)

screen = ['.']
chars = {35:'#', 46:'.', 94:'^', 60:'<', 62:'>', 118:'v'}
inc = {'end':10, ',':44, 'A':65, 'B':66, 'C':67, 'R':82, 'L':76, '0':48, 'y':121, 'n':110}

n = 0
for i in outputs:
    if i != 10:
        screen[n] += chars[i]
    elif i == 10:
        screen[n] += '.'
        screen.append('.')
        n += 1

del screen[-2:]
screen.insert(0, '.' * len(screen[0]))
screen.append('.' * len(screen[0]))

#part 1:
screeninter = screen.copy()

s = 0

for i in range(1, len(screen) - 1):
    for j in range(1, len(screen[i]) - 1):
        if screen[i][j] == '#':
            if screen[i + 1][j] == screen[i][j + 1] == screen[i - 1][j] == screen[i][j - 1] == '#':
                s += ((i - 1) * (j - 1))
                screeninter[i] = screeninter[i][:j] + 'O' + screeninter[i][j + 1:]

    print(screeninter[i])
#print(s)

#part 2:
directions = []
for i in range(len(screen)):
    for j in range(len(screen[i])):
        if screen[i][j] == '^':
            x = j
            y = i
            d = 3
            break

def diradd(addition):
    global d
    d += addition
    if d > 3:
        d = 0
    elif d < 0:
        d = 3
    if addition > 0:
        return 'R'
    elif addition < 0:
        return 'L'

while True:
    #print(d)
    if d == 0: #right
        if screen[y][x + 1] == '#':
            x += 1
            directions[-1] += 1
        elif screen[y][x + 1] == '.':
            if screen[y - 1][x] == '#':
                directions.append(diradd(-1))
            elif screen[y + 1][x] == '#':
                directions.append(diradd(1))
            else:
                break
            directions.append(0)
    elif d == 1: #down
        if screen[y + 1][x] == '#':
            y += 1
            directions[-1] += 1
        elif screen[y + 1][x] == '.':
            if screen[y][x - 1] == '#':
                directions.append(diradd(1))
            elif screen[y][x + 1] == '#':
                directions.append(diradd(-1))
            else:
                break
            directions.append(0)
    elif d == 2: #left
        if screen[y][x - 1] == '#':
            x -= 1
            directions[-1] += 1
        elif screen[y][x - 1] == '.':
            if screen[y - 1][x] == '#':
                directions.append(diradd(1))
            elif screen[y + 1][x] == '#':
                directions.append(diradd(-1))
            else:
                break
            directions.append(0)
    elif d == 3: #up
        if screen[y - 1][x] == '#':
            y -= 1
            directions[-1] += 1
        elif screen[y - 1][x] == '.':
            if screen[y][x - 1] == '#':
                directions.append(diradd(-1))
            elif screen[y][x + 1] == '#':
                directions.append(diradd(1))
            else:
                break
            directions.append(0)

#print(directions)

#i did this part manually because i couldn't be bothered to code an actual solution
routines = {'A':'R6R6R8L10L4',
            'B':'R6L10R8',
            'C':'L4L12R6L10'}
order = 'ABBACACACB'

def convert(l):
    newlist = []
    double = False
    for i in l:
        if i in [str(s) for s in range(11)]:
            newlist.append(inc['0'] + int(i))
            double = True
        else:
            if double:
                newlist.append(inc[','])
                double = False
            newlist.append(inc[i])
            newlist.append(inc[','])
    if not double:
        del newlist[-1]
    newlist.append(inc['end'])
    return newlist


o = original.copy()
o[0] = 2
for i in range(1000000):
    o.append(0)
input = []
input += convert(order)
input += convert(routines['A'])
input += convert(routines['B'])
input += convert(routines['C'])
input.append(inc['n'])
input.append(inc['end'])
outputs = []

print(input)

n = 0
go = True
while go:
    #print(n)
    n = parse(n)
    #print(inputindex)

print(outputs[-1])

#i really struggled on this one
#i used an online ascii converter for the errors because i suck

original = [int(s) for s in input().split(',')]
o = original.copy()
for i in range(1000000):
    o.append(0)

relbase = 0

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
        print('assignfail')

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
        o[a] = input
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

painted = {}
input = 1
outputs = []
x, y = 0, 0
painted[(0, 0)] = input

dir = 1

def rotate(dir):
    global x, y
    if dir == 0:
        x += 1
    elif dir == 1:
        y += 1
    elif dir == 2:
        x -= 1
    elif dir == 3:
        y -= 1



n = 0
while go:
    n = parse(n)
    if len(outputs) == 2:
        painted[(x, y)] = outputs[0]

        if outputs[1] == 0:
            dir += 1
            if dir == 4:
                dir = 0
        elif outputs[1] == 1:
            dir -= 1
            if dir == -1:
                dir = 3
        rotate(dir)
        #print(x, y)
        if (x, y) not in painted.keys():
            painted[(x, y)] = 0
        input = painted[(x, y)]
        outputs = []

#print(len(painted.keys()))
#print(painted)

#part 2:
for y in range(-5, 1):
    string = ''
    for x in range(50):
        if (x, y) in painted.keys():
            if painted[(x, y)] == 0:
                string += '.'
            elif painted[(x, y)] == 1:
                string += '#'
        else:
            string += '.'
    print(string)


#LMAO it comes out upside down 

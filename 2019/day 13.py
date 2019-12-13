original = [int(s) for s in input().split(',')]
#with open('input.txt', 'r') as f:
#    original = f.read().split(',')

o = original.copy()
for i in range(10000):
    o.append(0)

#input = 0
relbase = 0
outputs = []

def assignpara(oc, ocpos, opos, c):
    #print(oc, ocpos, opos)
    if oc[ocpos] == 0:
        #print(n, opos, o[n + opos])
        #print(o[n + opos])
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
        print('ass')

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
        a = assignpara(oc, -3, 1, True)
        draw()
        #inp = int(input('input: '))
        #inp -= 2 #so i can use 123 as input
        #print(ball, paddle)
        if ball > paddle:
            inp = 1
        elif ball == paddle:
            inp = 0
        elif ball < paddle:
            inp = -1


        o[a] = inp
        #global input
        #input = input('Input: ')
        
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
        print('fuck')

tilelist = {'0':' ', '1':'=', '2':'□', '3':'-', '4':'O'}
tiles = [['' for t in range(37)] for s in range(22)]
score = 0
ball = 0
paddle = 0

def draw():
    global outputs
    #print(outputs)
    for i in range(0, len(outputs) - 2, 3):
        if outputs[i] == -1 and outputs[i + 1] == 0:
            global score
            score = outputs[i + 2]
        else:
            tiles[outputs[i + 1]][outputs[i]] = str(outputs[i + 2])
            if outputs[i + 2] == 4:
                global ball
                #print(ball)
                ball = outputs[i]
            if outputs[i + 2] == 3:
                global paddle
                #print(paddle)
                paddle = outputs[i]
    for i in tiles:
        row = ''
        for j in range(len(i)):
            row += tilelist[str(i[j])]
        print(row)
    print('Score:', str(score))
    outputs = []


go = True
n = 0
while go:
    #print(n)
    n = parse(n)

draw()



#part one:
#tiles = ['' for s in range(22)]
#for i in range(0, len(outputs) - 3, 3):
    #tiles[outputs[i + 1]] += str(outputs[i + 2])
    #if outputs[i + 2] == 2:
        #blockcount += 1
#print(blockcount)

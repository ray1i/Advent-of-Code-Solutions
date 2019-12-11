original = [int(s) for s in input().split(',')]
o = original.copy()
for i in range(1000000):
    o.append(0)

input = 2
relbase = 0
outputs = []


go = True

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
            #print('one')
            #print(c)
            o[c] = a + b 
        elif oc[-1] == 2:
            #print('two')
            o[c] = a * b
        return n + 4

    elif oc[-1] == 3:
        #print('three')
        #print(a, relbase, o[n + 1])
        a = assignpara(oc, -3, 1, True) #special case
        o[a] = input
        return n + 2
        #print(n)

    elif oc[-1] == 4:
        #print('four')
        outputs.append(a)
        #print(n, a)
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
        #print('nine', relbase, a)
        #global relbase
        relbase += a
        return n + 2

    elif oc[-1] == 9 and oc[-2] == 9:
        #print('fuckign end')
        global go
        go = False
        return n + 1
        
    else:
        print('fuck')

n = 0
while go:
    #print(o, n, relbase)
    #print(n, relbase)
    n = parse(n)

print(outputs)

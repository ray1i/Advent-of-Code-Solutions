import itertools

original = [int(s) for s in input().split(',')]

def assignpara(o, oc, ocpos, opos, n):
    #print(opos)
    if oc[ocpos] == 0:
        return o[o[n + opos]]
    elif oc[ocpos] == 1:
        return o[n + opos]
    else:
        print('ass')

def parse(o, n, pinput, j):
    #print(pinput)
    oc = str(o[n])
    if len(oc) < 5:
        oc = (5-len(oc))*'0' + oc
    oc = [int(s) for s in oc]

    if oc[-1] == 1 or oc[-1] == 2:
        a = 0
        b = 0
        a = assignpara(o, oc, -3, 1, n)
        b = assignpara(o, oc, -4, 2, n)
        if oc[-1] == 1:
            #print('one')
            c = a + b 
        elif oc[-1] == 2:
            #print('two')
            c = a * b

        o[o[n + 3]] = c
        return n + 4

    elif oc[-1] == 3:
        global inputnum
        o[o[n + 1]] = pinput[inputnum[j]]
        #print('three', j, n)
        inputnum[j] += 1
        return n + 2
        #print(n)

    elif oc[-1] == 4:
        a = assignpara(o, oc, -3, 1, n)
        #print('four')
        global outputs
        outputs[j].append(a)
        #print(outputs, j)
        return n + 2
    
    elif oc[-1] == 5 or oc[-1] == 6:
        a = 0
        b = 0
        a = assignpara(o, oc, -3, 1, n)
        b = assignpara(o, oc, -4, 2, n)
        
        if oc[-1] == 5:
            #print('five', j, n, a)
            if a != 0:
                return b
        elif oc[-1] == 6:
            if a == 0:
                return b
        return n + 3

    elif oc[-1] == 7:
        a = 0
        b = 0
        a = assignpara(o, oc, -3, 1, n)
        b = assignpara(o, oc, -4, 2, n)
        if a < b:
            o[o[n+3]] = 1
        else: 
            o[o[n+3]] = 0
        return n + 4
    
    elif oc[-1] == 8:
        a = 0
        b = 0
        a = assignpara(o, oc, -3, 1, n)
        b = assignpara(o, oc, -4, 2, n)
        if a == b:
            o[o[n+3]] = 1
        else:
            o[o[n+3]] = 0
        return n + 4

    elif oc[-1] == 9 and oc[-2] == 9:
        #print('fuckign end')
        global go
        go[j] = False
        return n
        
    else:
        print('fuck')

phasesettings = list(itertools.permutations([5,6,7,8,9]))

maxout = -1

for ps in phasesettings:
#for i in range(1):
    phasesetting = list(ps)
    
    #phasesetting = [9,8,7,6,5]
    
    outputs = [[] for s in range(5)]
    o = []
    for i in range(5):
        o.append(original.copy())
    lastoutputs = []

    input = 0
    inputs = []
    for i in range(5):
        inputs.append([phasesetting[i]])
    inputs[0].append(input)

    inputnum = [0 for s in range(5)]
    n = [0 for s in range(5)]
    go = [True for s in range(5)]

    j = 0
    while go != [False, False, False, False, False]:
        if go[j]:
            #print(n)
            try:
                n[j] = parse(o[j], n[j], inputs[j], j)
                if j < 4:
                    for i in range(len(outputs[j])):
                        inputs[j + 1].append(outputs[j][i])
                    outputs[j] = []
                elif j == 4:
                    for i in range(len(outputs[j])):
                        inputs[0].append(outputs[j][i])
                        lastoutputs.append(outputs[j][i])
                    outputs[j] = []
            except IndexError:
                if j < 4:
                    for i in range(len(outputs[j])):
                        inputs[j + 1].append(outputs[j][i])
                    outputs[j] = []
                    j += 1
                elif j == 4:
                    for i in range(len(outputs[j])):
                        inputs[0].append(outputs[j][i])
                        lastoutputs.append(outputs[j][i])
                    outputs[j] = []
                    j = 0
        else:
            if j < 4:
                j += 1
            else:
                j = 0
        #print(j)
        #print(go)
    
    if lastoutputs[-1] > maxout:
        maxout = lastoutputs[-1]
        #print('gottem', outputs[4][-1])

print(maxout)

import math

rxninp = {}
rxnout = {}

CHECK = 0
while CHECK != '12 GLZH => 5 LHVTN':
    CHECK = input()
    inp = CHECK.split(' => ')

    output = inp[-1].split()
    rxnout[output[-1]] = int(output[0])

    rxninp[output[-1]] = []
    chems = inp[0].split(', ')
    for i in range(len(chems)):
        gem = chems[i].split()
        rxninp[output[-1]].append((int(gem[0]), gem[-1]))

#print(rxninp)
#print(rxnout)

exist = {}
extra = {}
for i in rxnout.keys():
    exist[i] = 0
    extra[i] = 0
for i in rxninp['FUEL']:
    exist[i[1]] = i[0]
exist['ORE'] = 0
extra['ORE'] = 0

#print(exist)
#print(extra)

#part one:

gocount = 0

while gocount != len(exist.keys()) - 1:
    for i in exist.keys():
        #print(exist, extra)
        if i != 'ORE' and exist[i] != 0:
            if extra[i] >= exist[i]:
                extra[i] -= exist[i]
                exist[i] = 0
            else:
                times = int(math.ceil((exist[i] - extra[i]) / rxnout[i]))
                for j in rxninp[i]:
                    exist[j[1]] += j[0] * times
                extra[i] += rxnout[i] * times - exist[i]
                exist[i] = 0
        
    gocount = 0
    for i in exist.keys():
        if exist[i] == 0 and i != 'ORE':
            gocount += 1
    
complete = exist['ORE']

print(complete)

#part two:

trillion = 1000000000000
cargo = trillion
fuelcount = 0

exist = {}
for i in rxnout.keys():
    exist[i] = 0
for i in rxninp['FUEL']:
    exist[i[1]] = i[0]
exist['ORE'] = 0

gocount = 0
while gocount != len(exist.keys()) - 1:
    for i in extra.keys():
        if i != 'ORE' and extra[i] != 0:
            ratio = extra[i] / rxnout[i]
            for j in rxninp[i]:
                extra[j[1]] += ratio * j[0]
            extra[i] = 0
        
    gocount = 0
    for i in extra.keys():
        if extra[i] == 0 and i != 'ORE':
            gocount += 1
    print(extra)

print(extra['ORE'])
print(trillion // (complete - extra['ORE']))



#this took too long, scrapped:
'''
while cargo > 0:
    gocount = 0
    exist = {}
    for i in rxnout.keys():
        exist[i] = 0
    for i in rxninp['FUEL']:
        exist[i[1]] = i[0]
    exist['ORE'] = 0

    while gocount != len(exist.keys()) - 1:
        for i in exist.keys():
            #print(exist, extra)
            if i != 'ORE' and exist[i] != 0:
                if extra[i] >= exist[i]:
                    extra[i] -= exist[i]
                    exist[i] = 0
                else:
                    times = int(math.ceil((exist[i] - extra[i]) / rxnout[i]))
                    for j in rxninp[i]:
                        exist[j[1]] += j[0] * times
                    extra[i] += rxnout[i] * times - exist[i]
                    exist[i] = 0
            
        gocount = 0
        for i in exist.keys():
            if exist[i] == 0 and i != 'ORE':
                gocount += 1

    fuelcount += 1
    cargo -= exist['ORE']
    exist['ORE'] = 0
    print(cargo)

    extracount = 0
    for i in extra.keys():
        if extra[i] == 0:
            extracount += 1
    if extracount == len(extra.keys()):
        whole = trillion - cargo
        mostofit = trillion // whole
        cargo = trillion - (mostofit * whole)
        
        ratio = fuelcount 
        fuelcount = ratio * mostofit
    
'''

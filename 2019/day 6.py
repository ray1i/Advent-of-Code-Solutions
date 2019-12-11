end = 'M2K)4HD'
k = 0
orbits = []

while k != end:
    k = input('enter')
    orbits.append(k)

o = {}

for i in range(len(orbits)):
    a = orbits[i].split(')')
    o[a[1]] = a[0]

''' #Part one
bigcount = 0

for key in o:
    ke = key
    while ke != 'COM':
        ke = o[ke]
        bigcount += 1
        #print(ke, o[key])

print(bigcount)
'''

#Part two:
me = []

ke = 'YOU'
while ke != 'COM':
    ke = o[ke]
    me.append(ke)


santa = []
ke = 'SAN'
while ke != 'COM':
    ke = o[ke]
    santa.append(ke)

common = 'gay'

for i in me:
    for j in santa:
        if i == j and common == 'gay' and j != 'COM':
            common = i
            break

bigcount = 0

ke = 'YOU'
while ke != common:
    #print(common)
    #print(ke)
    ke = o[ke]
    bigcount += 1

ke = 'SAN'
while ke != common:
    #print(ke)
    ke = o[ke]
    bigcount += 1

print(bigcount - 2, common)




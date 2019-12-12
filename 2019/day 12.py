import copy

opos = []
for i in range(4):
    m = input().split(',')
    mo = []
    for j in range(2):
        mo.append(int(m[j][3:]))
    mo.append(int(m[2][3:-1]))
    opos.append(mo)

pos = copy.deepcopy(opos)
vel = [[0, 0, 0] for s in range(4)]

def velchange(moon, axis):
    for i in range(4):
        if i != moon:
            if pos[i][axis] > pos[moon][axis]:
                vel[moon][axis] += 1
            elif pos[i][axis] < pos[moon][axis]:
                vel[moon][axis] -= 1

def movemoon(moon, axis):
    pos[moon][axis] += vel[moon][axis]

def findenergy(moon):
    posen = 0
    velen = 0
    for axis in range(3):
        posen += abs(pos[moon][axis])
        velen += abs(vel[moon][axis])
    return posen * velen


#part 1:
'''
for p in range(1000):
    for moon in range(4):
        for axis in range(3):
            velchange(moon, axis)
    for moon in range(4):
        for axis in range(3):
            movemoon(moon, axis)'''

#print(findenergy(0) + findenergy(1) + findenergy(2) + findenergy(3))

#part 2:
step = 0
x, y, z = 0, 0, 0
while True:
    step += 1
    for moon in range(4):
        for axis in range(3):
            velchange(moon, axis)
    for moon in range(4):
        for axis in range(3):
            movemoon(moon, axis)
    if (pos[0][0] == opos[0][0] and
        pos[1][0] == opos[1][0] and
        pos[2][0] == opos[2][0] and
        pos[3][0] == opos[3][0] and
        vel[0][0] == vel[1][0] == vel[2][0] == vel[3][0] == 0 and
        x == 0):
        x = step
        print('got x', x)
    if (pos[0][1] == opos[0][1] and
        pos[1][1] == opos[1][1] and
        pos[2][1] == opos[2][1] and
        pos[3][1] == opos[3][1] and
        vel[0][1] == vel[1][1] == vel[2][1] == vel[3][1] == 0 and
        y == 0):
        y = step
        print('got y', y)
    if (pos[0][2] == opos[0][2] and
        pos[1][2] == opos[1][2] and
        pos[2][2] == opos[2][2] and
        pos[3][2] == opos[3][2] and
        vel[0][2] == vel[1][2] == vel[2][2] == vel[3][2] == 0 and
        z == 0):
        z = step
        print('got z', z)
    if x != 0 and y != 0 and z != 0:
        break

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 
  
# Driver program to test above function 
print(lcm(x, lcm(y, z)), x, y, z)
  
# This code is contributed by Danish Raza 

#haha this code takes like a minute to run

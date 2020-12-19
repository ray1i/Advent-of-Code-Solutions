# c++ too hard :(

with open("17.txt", "r") as f:
    lines = []
    for line in f:
        lines.append(line.strip())

#part one:
cube = [[]] #z, y, x

for y in range(len(lines)):
    cube[0].append([])
    for x in range(len(lines[y])):
        if  lines[y][x] == '#':
            cube[0][y].append(True)
        else:
            cube[0][y].append(False)

def update_cube(c):
    new = [[[False for x in range(len(c[0][0]) + 2)] for y in range(len(c[0]) + 2)] for z in range(len(c) + 2)]
    for z in range(len(new)):
        for y in range(len(new[0])):
            for x in range(len(new[0][0])):
                total_surroundings = 0

                for dz in range(-1, 2):
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (dz, dy, dx) != (0, 0, 0) and z - 1 + dz >= 0 and y - 1 + dy >= 0 and x - 1 + dx >= 0:
                                try:
                                    if c[z - 1 + dz][y - 1 + dy][x - 1 + dx]:
                                        total_surroundings += 1
                                except IndexError:
                                    pass
                
                try:
                    if total_surroundings == 3:
                        new[z][y][x] = True
                    elif (total_surroundings == 2 or total_surroundings == 3) and c[z - 1][y - 1][x - 1] and z - 1 >= 0 and y - 1 >= 0 and x - 1 >= 0:
                        new[z][y][x] = True
                except:
                    pass
    return new

def count_active(c):
    count = 0
    for z in range(len(c)):
        for y in range(len(c[z])):
            for x in range(len(c[z][y])):
                if c[z][y][x]:
                    count += 1
    return count

cycles = 6
for i in range(cycles):
    cube = update_cube(cube)

print('part one:', count_active(cube))

#part two:
cube = [[[]]] #w, z, y, x
for y in range(len(lines)):
    cube[0][0].append([])
    for x in range(len(lines[y])):
        if  lines[y][x] == '#':
            cube[0][0][y].append(True)
        else:
            cube[0][0][y].append(False)

def update_cube2(c):
    new = [[[[False for x in range(len(c[0][0][0]) + 2)] for y in range(len(c[0][0]) + 2)] for z in range(len(c[0]) + 2)] for w in range(len(c) + 2)]
    for w in range(len(new)):
        for z in range(len(new[0])):
            for y in range(len(new[0][0])):
                for x in range(len(new[0][0][0])):
                    total_surroundings = 0

                    for dw in range(-1, 2):
                        for dz in range(-1, 2):
                            for dy in range(-1, 2):
                                for dx in range(-1, 2):
                                    if (dw, dz, dy, dx) != (0, 0, 0, 0) and w - 1 + dw >= 0 and z - 1 + dz >= 0 and y - 1 + dy >= 0 and x - 1 + dx >= 0:
                                        try:
                                            if c[w - 1 + dw][z - 1 + dz][y - 1 + dy][x - 1 + dx]:
                                                total_surroundings += 1
                                        except IndexError:
                                            pass
                    
                    try:
                        if total_surroundings == 3:
                            new[w][z][y][x] = True
                        elif (total_surroundings == 2 or total_surroundings == 3) and c[w - 1][z - 1][y - 1][x - 1] and w - 1 >= 0 and z - 1 >= 0 and y - 1 >= 0 and x - 1 >= 0:
                            new[w][z][y][x] = True
                    except:
                        pass
    return new

def count_active2(c):
    count = 0
    for w in range(len(c)):
        for z in range(len(c[w])):
            for y in range(len(c[w][z])):
                for x in range(len(c[w][z][y])):
                    if c[w][z][y][x]:
                        count += 1
    return count

def print_cube(c):
    for w in range(len(c)):
        for z in range(len(c[w])):
            for y in range(len(c[w][z])):
                for x in range(len(c[w][z][y])):
                    if c[w][z][y][x]:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
            print()
        print('------')

for i in range(cycles):
    cube = update_cube2(cube)

print('part two:', count_active2(cube))
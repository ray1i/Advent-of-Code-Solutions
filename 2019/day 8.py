original = input()

print(len(original))

h = 6
w = 25
l = h * w 

#print(len(original), (h * w))
if len(original) % (h * w) != 0:
    #print('yep')
    original += ('X' * (len(original) % (h*w)))

pix = []

for i in range(int(len(original) / l)):
    p = [[] for s in range(h)]
    for j in range(h):
        p[j].append(original[j * w + (i * l):(j + 1) * w + (i * l)])
    pix.append(p)

#print(pix)

maxzeros = 999999999999
maxlayer = 0
onetwo = [[0, 0] for s in range(len(pix))]

for layer in range(len(pix)):
    zeros = 0
    for i in range(h):
        for j in range(w):
            if pix[layer][i][0][j] == '0':
                zeros += 1
            elif pix[layer][i][0][j] == '1':
                #print(onetwo[i][0])
                onetwo[layer][0] += 1
            elif pix[layer][i][0][j] == '2':
                onetwo[layer][1] += 1
    if zeros < maxzeros:
        maxzeros = zeros
        maxlayer = layer

#print(onetwo)
#print(onetwo[maxlayer][0], onetwo[maxlayer][1])
print(onetwo[maxlayer][0] * onetwo[maxlayer][1])
        
#i did part two in processing:
'''
with open("C:\Users\mr251\Desktop\AOC 2019\input_day_8.txt", 'r') as f:
    original = f.read()
#original = input()

#print(len(original))



h = 6
w = 25
l = h * w 

#print(len(original), (h * w))
if len(original) % (h * w) != 0:
    #print('yep')
    original += ('X' * (len(original) % (h*w)))

pix = []

for i in range(int(len(original) / l)):
    p = [[] for s in range(h)]
    for j in range(h):
        p[j].append(original[j * w + (i * l):(j + 1) * w + (i * l)])
    pix.append(p)

#print(pix)

picture = []
for i in range(h):
    picture.append(['2' for s in range(w)])
colours = {'0':'#ffffff', '1':'#000000'}

for layer in range(len(pix)):
    for i in range(h):
        for j in range(w):
            #print(i, j)
            if pix[layer][i][0][j] == '0' and picture[i][j] == '2':
                picture[i][j] = '0'
            elif pix[layer][i][0][j] == '1' and picture[i][j] == '2':
                picture[i][j] = '1'

def setup():
    size(w * 10, h * 10)

def draw():
    rectMode(CORNER)
    for i in range(h):
        for j in range(w):
            print(colours[picture[i][j]], i, j)
            fill(colours[picture[i][j]])
            rect(j * 10, i * 10, 10, 10)
'''

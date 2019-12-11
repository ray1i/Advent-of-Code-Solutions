c = 0
double = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']
num = [int(s) for s in input().split('-')]

a = False
b = False

def checka(n):
    nn = list(map(int, str(n)))
    #print(nn, sorted(nn))
    return nn == sorted(nn)
    

for i in range(num[0], num[1] + 1):
    print(i)
    if checka(i):
        b = True
        #print('b')
        for j in double:
            if j in str(i):
                if j + j[0] not in str(i):
                    a = True
                #print('yes')
    if a and b:
        c += 1
    a = False
    b = False

print(c)
            

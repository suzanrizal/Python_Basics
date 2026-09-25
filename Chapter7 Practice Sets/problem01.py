
def highest(a,b,c):
    if(a>b)and(a>c):
        return a
    elif(b>a)and(b>c):
        return b
    elif(c>a)and(c>b):
        return c


a = 12
b = 2
c = 33

print(highest(a,b,c))


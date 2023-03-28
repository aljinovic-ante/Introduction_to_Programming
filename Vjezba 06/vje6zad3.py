def srednji(a,b,c):
    if(a>b>c):
        return b
    elif(a>c>b):
        return c
    elif(b>a>c):
        return a
    elif(b>c>a):
        return c
    elif(c>a>b):
        return a
    elif(c>b>a):
        return b
    
a=int(input("Unesite drugi broj: "))
b=int(input("Unesite drugi broj: "))
c=int(input("Unesite drugi broj: "))

s=srednji(a,b,c)

print(s)
        
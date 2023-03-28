def kordinate(k):
    a,b,c=k
    if a<=b<=c:
        print(a,b)
    elif a<=c<=b:
        print(a,c)
    elif b<=a<=c:
        print(b,a)
    elif b<=c<=a:
        print(b,c)
    elif c<=a<=b:
        print(c,a)
    elif c<=b<=a:
        print(c,b)

k=(1,3,2)
kordinate(k)
x=int(input("Unesite prvi broj: "))
y=int(input("Unesite drugi broj: "))
if x>0 and y>0:
    if x>y:
        for i in range (y+1,x):
            print(i)
    if y>x:
        for i in range (x+1,y):
            print(i)
else:
    print("Greška")
x = input("Unesite broj: ")
y = input("Unesite broj: ")
z = input("Unesite broj: ")

if(x>y and x>z and y>z):
    print(x,y,z)
elif(x>y and x>z and z>y):
    print(x,z,y)

if(y>x and y>z and x>z):
    print(y,x,z)
elif(y>x and y>z and z>x):
    print(y,z,x)
    
if(z>x and z>y and x>z):
    print(z,x,y)
elif(z>x and z>y and z>x):
    print(z,y,x)
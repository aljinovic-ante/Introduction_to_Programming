x=int(input("Unesite broj: "))

brbit=0
suma=0

while(x!=0):
    if(x&1==1):
        brbit+=1
    x=x>>1
    
for i in range(brbit):
    y=int(input("Unesite broj: "))
    suma=suma+y
    
print(suma)
br=0
par=0
nep=0
while(br<10):
    broj=int(input("Unesite broj: "))
    if(broj!=0):
        br+=1
        if(broj%2==0):
            par+=1
        else:
            nep+=1
print("Broj parnih brojeva:",par,"Broj neparnih brojeva:",nep)   
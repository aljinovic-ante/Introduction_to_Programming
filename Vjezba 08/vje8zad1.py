def brdjel(broj):
    brojac=0
    for i in range(2,broj):
        if broj%i==0:
            brojac+=1
    return brojac

x=int(input("Unesite broj: "))
while(brdjel(x)<3):
    x=int(input("Unesite broj: "))
    
print(brdjel(x))
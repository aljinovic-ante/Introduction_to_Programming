brojac=0
x=int(input("Unesite broj: "))
for i in range (0,32):
    if (x>>i & 1 == 1):    
      brojac += 1
print(brojac)
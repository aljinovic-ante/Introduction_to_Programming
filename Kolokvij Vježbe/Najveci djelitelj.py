a=int(input("Upisite brojnik: "))
b=int(input("Upisite nazivnik: "))
for i in range (a,1,-1):
    if a%i==0 and b%i==0:
        brojnik=a//i
        nazivnik=b//i
        print(brojnik,nazivnik)
        break

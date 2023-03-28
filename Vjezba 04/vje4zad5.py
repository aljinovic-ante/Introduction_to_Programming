neg=0

while True:
    broj = int(input("Unesite broj: "))
    if broj < 0:
        neg += 1
    elif broj == 0:
        break
print("Broj negativnih unosa: ", neg)
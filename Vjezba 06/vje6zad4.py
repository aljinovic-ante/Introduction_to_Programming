broj=int(input("Unesite broj: "))
mjesto=int(input("Unesite mjesto: "))

def funkcija(broj, mjesto):
    for i in range(mjesto-1):
        broj=broj//10
    return broj%10
print(funkcija(broj,mjesto))
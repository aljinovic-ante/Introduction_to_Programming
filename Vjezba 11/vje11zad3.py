lista1=[5,8,3,7,2,4,6,1]
lista2=[True]

def funkcija():
    for i in range(1, len(lista1)):
        if lista1[i] > lista1[i-1]:
            lista2.append(True)
        else:
            lista2.append(False)
            
funkcija()
print(lista1)
print(lista2)
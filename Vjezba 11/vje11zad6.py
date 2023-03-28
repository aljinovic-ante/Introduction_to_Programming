rjecnik = {}
lista1 = ["Danas","je","lijep","suncan","dan"]
lista2 = ["Jucer","je","bio","suncan","dan"]

def funkcija():
    for i in range(len(lista1)):
      if lista2[i]==lista1[i]:
        rjecnik[lista1[i]] = True
      else:
        rjecnik[lista1[i]] = False
    print(rjecnik)
    
funkcija()
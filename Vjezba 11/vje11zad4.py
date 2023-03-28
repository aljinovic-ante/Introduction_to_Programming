lista1=["ime.prezime@unist.hr","petarkresimir.ivanovic@unista.hr", "marko.markic@unist.hr"]
lista2=[]

def funkcija():
    for i in range(len(lista1)):
        a, b = lista1[i].split("@")
        ime, prezime = a.split(".")
        if len(ime)<=10 and len(prezime)<=10:
            lista2.append(lista1[i])

funkcija()
print(lista2)
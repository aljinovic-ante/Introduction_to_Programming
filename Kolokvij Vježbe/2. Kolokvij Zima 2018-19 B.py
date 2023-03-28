# -*- coding: utf-8 -*-
"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) B
"""

#Zadatak 1 --> Vj9zad1

#Zadatak 2 --> v10zad4

#Zadatak 3
#Napisati funkciju koja prima matricu (listu lista) i vraca listu sastavljenu
#od svih brojeva u matrici.

def matricaulistu (matrica):
    lst=[]
    for i in matrica:
        for e in i:
            lst.append(e)
    return lst

print(matricaulistu([[1,2,3], [4,5,6], [7,8,9]]))

#Zadatak 4
#Napisati funkciju koja prima rjecnik koji kao kljuceve ima brojeve, a kao
#vrijednosti liste brojeva. Funkcija vraca True ako je svaki kljuc jednak
#prosjeku brojeva u pridruženoj listi.

def prosjeci(rjecnik):
    for k in rjecnik:
        z = 0
        for e in rjecnik[k]:
            z += e
        if k != z / len(rjecnik[k]):
            return False
    return True

rjecnik = { 15: [10, 15, 20], 20: [15, 25 ], 12: [16, 8] }
print(prosjeci(rjecnik))
# -*- coding: utf-8 -*-
"""
2. Kolokvij Zima 2017-18 B
"""

#Zadatak 1 --> 1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) C Zadatak 3

#Zadatak 2
#Napisati funkciju koja prima jedan string. String može biti „X plus Y“ ili
#„X minus Y“, gdje su X i Y dva cijela broja (mogu imati više znamenki
#ili predznak). Funkcija vraca zbroj ili razliku brojeva X i Y.

def racuna(string):
    lst=string.split(" ")
    a,b=int(lst[0]), int(lst[2])
    if lst[1]=="minus":
        return a-b
    else:
        return a+b

print(racuna("-20 plus 3"))
print(racuna("4 minus 1"))

#Zadatak 3 --> Vj11Zad1

#Zadatak 4
#Napisati funkciju koja prima rjecnik i jedan broj. Vrijednosti u rjecniku
#su liste brojeva. Funkcija vraca True ako se broj nalazi negdje u rjecniku.

def urjecniku(rjecnik,n):
    if any(n in v for v in rjecnik.values()):
        return True
    else:
        return False


rjecnik={"a":[1,2],"b":[3,4],"c":[5,6]}
print(urjecniku(rjecnik,4))
print(urjecniku(rjecnik,7))



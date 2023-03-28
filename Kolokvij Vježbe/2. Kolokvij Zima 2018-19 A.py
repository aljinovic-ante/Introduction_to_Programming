# -*- coding: utf-8 -*-
"""
#1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) A
"""

#1.zadatak --> Vj11zad2

#2.zadatak
#Napisati funkciju koja prima string sastavljen od malih slova. Funkcija
#vraca string gdje su svi dvostruki suglasnici zamijenjeni jednim suglasnikom.
#Npr. za string "lookk", funkcija ce vratiti "look".

def dvostruki(string):
    rez=string[0]
    samoglasnici="aeiou"
    for c in string[1:]:
        if c not in samoglasnici and c != rez[-1]:
            rez += c
        elif c in samoglasnici:
            rez += c
    return rez

print(dvostruki("bbaaalloonn"))

#3. zadatak --> V11zad4

#4. zadatak
#Napisati funkciju koja prima rjecnik i broj B. Vrijednosti u rjecniku su
#liste brojeva. Funkcija vraca True ako su svi brojevi u svim listama u
#rjecniku manji od B.

def manjiodB (rjecnik,B):
    for keys,values in rjecnik.items():
        for i in values:
            if i < B:
                flag=True
            else:
                flag=False
    return flag

print(manjiodB({"1":[1,2,3], "2":[4,5,6], "3":[7,8,9]}, 10))
print(manjiodB({"1":[1,2,3], "2":[4,5,6], "3":[7,8,9]}, 9))



        
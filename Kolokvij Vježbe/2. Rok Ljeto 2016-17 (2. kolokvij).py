# -*- coding: utf-8 -*-
"""
2. Rok Ljeto 2016-17 (2. kolokvij)
"""

#Zadatak1
#Napisati funkciju koja prima listu brojeva. Funkcija ce vratiti dvije liste
#koje ce sadržati parne i neparne brojeve iz primljene liste.

def dvije(lst):
    parna=[]
    neparna=[]
    for e in lst:
        if e%2:
            parna.append(e)
        else:
            neparna.append(e)
    return parna, neparna
            
lst=[1,2,3,4,5,6,7]
print(dvije(lst))

#Zadatak 2--> Vj10Zad4

#Zadatak 3 --> Vj10Zad1

#Zadatak 4 --> 1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) A Zadatak 4


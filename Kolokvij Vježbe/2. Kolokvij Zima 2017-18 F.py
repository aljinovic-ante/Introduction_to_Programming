# -*- coding: utf-8 -*-
"""
2. Kolokvij Zima 2017-18 F
"""

#Zadatak 1
#Napisati funkciju koja prima listu brojeva. Funkcija vraca listu brojeva iz
#primljene liste koji su nisu djeljivi sa nijednim drugim brojem iz primljene
#liste. Npr. za listu [ 6, 2, 7, 9 ], funkcija vraca listu [2,7,9].

def nisudjeljivi(lst):
    nova=[]
    for e in lst:
        brojac=0
        for j in lst:
            if e%j==0:
                brojac+=1
        if brojac==1:
            nova.append(e)
    return nova

lst=[4,2,2,3,7]
print(nisudjeljivi(lst))

#Zadatak 2 --> 1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) A Zadatak 2

#Zadatak 3 
#Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
#element u nizu ce biti dio originalnog stringa koji pocinje velikim slovom
#i završava tockom.

def rastavi(string):
    lst=[]
    poc=-1
    kraj=-1
    for i in range (len(string)):
        if string[i].isupper():
            poc=i
        elif string[i]==".":
            kraj=i
            lst.append(string[poc:kraj+1])
    return lst
        
string="Ako. niste Znali. Ovo je String."
print(rastavi(string))

#Zadatak 4 --> 2. Kolokvij Zima 2017-18 A Zadatak 4




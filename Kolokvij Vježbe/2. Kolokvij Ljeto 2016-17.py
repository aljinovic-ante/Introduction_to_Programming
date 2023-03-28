# -*- coding: utf-8 -*-
"""
2. Kolokvij Ljeto 2016-17
"""

#Zadatak 1
#Napisati funkciju koja prima listu brojeva. Funkcija vraca listu koja sadrži
#svaki broj samo jednom. Npr. za listu [6,5,6,4,8,4], funkcija vraca [6,5,4,8].

def samojednom(lst):
    nova=[]
    for e in lst:
        if e not in nova:
            nova.append(e)
    return nova
            

lst=[6,5,6,4,8,4]
print(samojednom(lst))

#Zadatak 2 --> 2. Kolokvij Zima 2017-18 B Zadatak 2

#Zadatak 3 -->Vj10Zad1

#Zadatak 4
#Napisati funkciju koja prima listu lista brojeva. Funkcija od brojeva u
#listi konstruira rjecnik koji kao kljuceve ima zbroj svake pojedine liste, a
#svakom kljucu je kao vrijednost pridružena ta lista.

def rjecnik(lstlst):
    r={}
    for e in lstlst:
        zbroj=0
        for j in e:
            zbroj+=j
        r[zbroj]=e
    return r

lstlst=[[1,2],[3,4],[5,6]]
print(rjecnik(lstlst))



# -*- coding: utf-8 -*-
"""
2. Kolokvij Zima 2017-18 E
"""

#Zadatak 1--> 2. Kolokvij Zima 2017-18 C Zadatak 1

#Zadatak 2--> 1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) D Zadatak 2

#Zadatak 3
#Napisati funkciju koja prima matricu (listu lista) i vraca listu sastavljenu
#od svih brojeva u matrici.

def vracalistu(matrica):
    lst=[]
    for i in matrica:
        for e in i:
            lst.append(e)
    return lst

matrica=[[1,2,3],[4,5,6],[7,8,9]]
print(vracalistu(matrica))

#Zadatak 4
#Napisati funkciju koja prima listu lista brojeva. Funkcija od brojeva u
#listi konstruira rjecnik koji kao kljuceve ima najveci broj iz svake pojedine
#liste, a svakom kljucu je kao vrijednost pridružena ta lista.

def rjecnik(lstlst):
    r={}
    r1={}
    for e in lstlst:
        najveci=0
        for j in e:
            if j>najveci:
                najveci=j
        r.update({najveci:e}) 
        r1[najveci]=e #na kolokviju možda triba bez update
    return r,r1

lstlst=[[1,2,3],[4,5,6],[7,8,9]]
print(rjecnik(lstlst))


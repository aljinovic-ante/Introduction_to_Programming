# -*- coding: utf-8 -*-
"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) C
"""

#Zadatak 1
#Napisati funkciju koja prima dvije liste brojeva iste dužine. Funkcija
#vraca isprepletene liste. Npr. za liste [1,3,5] i [2,4,6], funkcija vraca
#listu [1,2,3,4,5,6].

def isprepleti(lsta,lstb):
    nova=[]
    for i in zip(lsta,lstb):
        for e in i:
            nova.append(e)
    return nova

print(isprepleti( [1,3,5], [2,4,6]))

#Zadatak 2
#Napisati funkciju koja prima jedan string. String je u obliku „(A+B)**N“,
#gdje su A, B i N cijeli pozitivni brojevi. Funkcija vraca rezultat tog izraza.

def izracunaj(string):
    dijelovi=string.split(")")
    dio=dijelovi[0][1:]
    a,b=dio.split("+")
    a=int(a)
    b=int(b)
    n=int(dijelovi[1][2:])
    return (a+b)**n

print(izracunaj("(2+1)**3"))

#Zadatak 3
#Napisati funkciju koja prima listu lista. Funkcija vraca listu koja sadrži
#duljine svih primljenih lista. Npr. za [ [1,2], [], [2] ], funkcija
#vraca [2,0,1].

def duljine(lstlst):
    nova = []
    for l in lstlst:
        nova.append(len(l))
    return nova

print(duljine([[1,2,3],[1],[1,2]]))


#Zadatak 4
#Napisati funkciju koja prima niz brojeva i dodatni broj. Funkcija vraca
#rjecnik koji ce imati tri kljuca: ’vece’, ’manje’, ’jednako’. Vrijednost
#svakog kljuca je lista brojeva koji su veci, manji ili jednaki broju.

def velicine(niz,broj):
    rjecnik={}
    brojevi=niz.split(",")
    lstm=[]
    lstv=[]
    lstj=[]
    for z in range(1,len(brojevi)+1):
        if z < broj:
            lstm.append(z)
            rjecnik.update({"manje":lstm})
        elif z > broj:
            lstv.append(z)
            rjecnik.update({"vece":lstv})
        else:
            lstj.append(z)
            rjecnik.update({"jednako":lstj})
    return rjecnik

print(velicine("1,2,3,4,5,6,7,8,9",5))


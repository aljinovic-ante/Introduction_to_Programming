# -*- coding: utf-8 -*-
"""
1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) D
"""

#Zadatak 1 --> Vj9zad1

#Zadatak 2
#Napisati funkciju koja prima dva stringa i broj N. Funkcija vraca true ako
#prvi string sadrži N samoglasnika, a drugi string N suglasnika. Npr. za
#stringove „uzeti“, „abcde“ i N=3, funkcija vraca True.

def f(prvi,drugi,N):
    samoglasnici="aeiou"
    cnt=0
    cnt1=0
    for c in prvi:
        if c in samoglasnici:
            cnt += 1
    for c in drugi:
        if c not in samoglasnici:
            cnt1+=1
    if cnt==N and cnt1==N:
        return True
    else:
        return False


print(f("balon","puž",2))

#Zadatak 3
#Napisati funkciju koja primljeni string rastavlja na niz stringova. Svaki
#element u nizu ce biti dio originalnog stringa koji pocinje otvorenom i
#završava zatvorenom zagradom. Npr. za string "ab(cd)ef(g)", funkcija
#vraca [ "cd", "g" ].


def rastavi(string):
    lst=[]
    for i in range(len(string)):
        if string[i]=="(":
            dio=""
            while string[i+1] != ")":
                dio+= string[i+1]
                i+=1
            lst.append(dio)
    return lst

print(rastavi("ab(cd)ef(g)"))

def rastavi1(string):
    lst=[]
    poc=-1
    kraj=-1
    for i in range(len(string)):
        if string[i]=="(":
            poc=i+1
        elif string[i]==")":
            kraj=i-1
            lst.append(string[poc:kraj+1])
    return lst

print(rastavi1("ab(cd)ef(g)"))

      
#Zadatak 4
#Napisati funkciju koja prima rjecnik sa stringovima kao kljucevima i listama
#brojeva kao vrijednostima. Za svaki kljuc u rjecniku, funkcija racuna
#najveci broj iz pridružene liste. Funkcija vraca rjecnik sastavljen od istih
#kljuceva i pridruženih najvecih brojeva.

def najveci(rjecnik):
    for k,v in rjecnik.items():
        for e in v:
            veci=v[0]
            if e > veci:
                veci=e
        rjecnik[k]=veci
    return rjecnik

print(najveci({"prvi":[1,2,3], "drugi":[2,3,4], "treci":[4,5,6]}))










      
# -*- coding: utf-8 -*-
"""
2. Kolokvij Zima 2017-18 C
"""

#Zadatak 1
#Napisati funkciju koja prima listu brojeva i listu booleana jednake dužine.
#Lista booleana ima tocno dva elementa postavljena na True. Ta dva elementa
#oznacavaju pocetak i kraj liste brojeva koju funkcija treba „izbaciti“
#iz originalne liste (funkcija vraca novu listu). Na primjer, za liste [ 6, 2,
#8, 4, 9 ] i [ F, T, F, T, F ], funkcija vraca listu [ 6, 9 ].

def izbaci(lstbr,lstbool):
    cnt=0
    izbacena=[]
    for i in range(len(lstbool)):
        if lstbool[i]==True:
            izbacena.append(i)
            cnt+=1
    if cnt==2:
        lstbr=lstbr[:izbacena[0]]+lstbr[izbacena[1]+1:]
        return lstbr
    
lstbr=[6,2,8,4,9]
lstbool=[False,True,False,True,False]

print(izbaci(lstbr,lstbool))

#Zadatak 2
#Napisati program koji od korisnika cita slova. Ako korisnik ne upiše slovo
#program ponavlja unos. Ako korisnik upiše tocku, program završava i
#ispisuje broj upisanih suglasnika i samoglasnika.

unos=""
samoglasnici="aeiou"
cntsam=0
cntsug=0
while True:
    unos=input("Unesite slovo:")
    if not unos.isalpha() and not unos==".":
        unos=input("Ponovite unos:")
    if unos in samoglasnici:
        cntsam+=1
    if unos not in samoglasnici and unos.isalpha():
        cntsug+=1
    if unos==".":
        break

print("Suglasnika:",cntsug,"Samoglasnika:",cntsam)


#Zadatak 3 --> 1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) D Zadatak 3

#Zadatak 4 --> 1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) D Zadatak 4

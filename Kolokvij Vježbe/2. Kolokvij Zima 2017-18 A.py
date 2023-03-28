# -*- coding: utf-8 -*-
"""
2. Kolokvij Zima 2017-18 A
"""

#Zadatak 1
#Napisati funkciju koja prima dvije liste brojeva. Funkcija vraca listu sa
#brojevima koji se pojavljuju u prvoj, ali ne i u drugoj listi. Npr. za liste
#[6, 2, 7, 9 ] i [2, 4, 5, 7], funkcija vraca listu [6, 9].

def uprvoj(lsta,lstb):
    nova=[]
    for i in lsta:
        if i not in lstb:
            nova.append(i)
    return nova


lsta=[6,2,7,9]
lstb=[2,4,5,7]
print(uprvoj(lsta,lstb))

#Zadatak 2-->1. Rok (2. Kolokvij) Zima 2018-19 (31.1.2019) D Zadatak 2

#Zadatak 3
#Napisati funkciju koja prima paran broj N i vraca matricu velicine NxN
#ispunjenu sa jedinicama i nulama. Gornja polovica matrice je ispunjena
#jedinicama.

def umatricu(N):
    matrica=[]
    k=0
    for i in range(N):
        redak=[]
        for j in range(N):
            if k<(N*N)/2:
                redak.append(1)
                k+=1
            else:
                redak.append(0)
        matrica.append(redak)
    return matrica
  
matrica=umatricu(8)          
for r in matrica:
    print(r)
    
#Zadatak 4
#Napisati funkciju koja prima rjecnik koji kao kljuceve ima brojeve, a kao
#vrijednosti liste brojeva. Funkcija vraca True ako je svaki kljuc jednak
#zbroju pridružene liste.

def jednakzbroju(rjecnik):
    for k in rjecnik:
        zbroj=0
        for e in rjecnik[k]:
            zbroj+=e
        if k!=zbroj:
            return False
    return True
        
rjecnik={3:[1,2],4:[2,2], 5:[1,4]}
print(jednakzbroju(rjecnik))


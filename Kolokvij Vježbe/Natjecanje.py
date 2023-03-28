# -*- coding: utf-8 -*-
"""
Napisati program koji od korisnika cita dva po dva broja, ukupno 20 
brojeva. Svaka dva broja predstavljaju rezultat nekog natjecanja i 
mogu biti (1,0), (0,1) ili (0.5,0.5). Ako uneseni brojevi nisu
ispravni, program ispisuje gresku i traži ponovan unos. Na kraju 
program ispisuje ukupan zbroj prvih i ukupan zbroj drugih brojeva.
"""

br=0
c=0
d=0
while br<10:
    a=float(input("1.broj: "))
    b=float(input("2.broj: "))
    k=(a,b)
    if (a==1 and b==0) or (b==1 and a==0) or (b==0.5 or a==0.5):
        br+=1
        c+=a
        d+=b
        k2=(c,d)
    else:
        print("Greska, ponovan upis")
if br==10:
    print(k2)
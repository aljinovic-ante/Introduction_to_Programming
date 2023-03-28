"""
Napisati funkciju koja čita dva po dva broja dok god korisnik
ne upiše oba pozitivna broja. Funkcija nakon toga vraća ta dva broja.

"""


def dvapodva():
    while True:
        a=int(input("1.Broj: "))
        b=int(input("2.Broj: "))
        if a>0 and b>0:
            return a,b
    
print(dvapodva())
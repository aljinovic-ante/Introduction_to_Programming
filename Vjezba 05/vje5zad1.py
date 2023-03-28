brojevi=0
from random import randint
while brojevi<10:
    x=randint(0,1001)
    if 100<x<500:
        print(x)
        brojevi+=1
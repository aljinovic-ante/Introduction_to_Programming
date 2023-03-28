def funkcija(p):
    import random
    x=random.randint(1,101)
    if p == "par":
        while x%2!=0:
            x=random.randint(1,101)
    elif p == "nepar":
        while x%2==0:
            x=random.randint(1,101)
    return(x)
    
print(funkcija("nepar"))
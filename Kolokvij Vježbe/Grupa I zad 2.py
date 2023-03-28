def rek_vrati(a,b):
    if a==0 or b==0:
        return 0
    while a>0 or b>0:
        if a%10==b%10:
            return 0 + rek_vrati(a//10, b//10)
        else:
            return 1 + rek_vrati(a//10, b//10)
    
print(rek_vrati(36415,32816))
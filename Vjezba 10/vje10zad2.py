def funkcija(lista):
    listaBr=[]
    listaStr=[]
    for e in lista:
        a,b=e
        listaBr.append(a)
        listaStr.append(b)
    
    return listaBr, listaStr
    
lst=[(1,"a"),(2,"b"),(3,"c")]
print(funkcija(lst))

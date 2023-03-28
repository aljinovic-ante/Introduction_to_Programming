def funkcija(a,b):
    lista=[]
    for i in a:
        for j in b:
            if i == j:
                lista.append(i)
    return lista

lst1=["Ako", "me", "ostavis", "kad", "pozelis", "kraj"]
lst2=["Ako", "me", "ostavis", "ne", "rusi", "drugo", "sve"]
print(funkcija(lst1,lst2))
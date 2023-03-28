def funkcija(lst):
    string=""
    for i in range(len(lst)):
        if lst[i] != ",":
            string = string+lst[i]
        else:
            pass
    return string

lst="Ako, me, ostavis"
print(funkcija(lst))
        
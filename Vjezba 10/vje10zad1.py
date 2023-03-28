def funkcija(a,b):
    l=len(a)
    for i in range(l):
        try:
            print(b[a[i]])
        except:
            print("Error")
        

lst1=[0,1,24,3,2]
lst2=["a","b","c","d","e","f","h"]
funkcija(lst1,lst2)
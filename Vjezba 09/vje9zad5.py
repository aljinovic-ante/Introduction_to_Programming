def srednjaVrijednost(lst1,lst2):
    pro=0
    for e in lst1:
        pro=pro+e
    pro=pro/len(lst1)
    for e in lst2:
        if e>pro:
            print(e)


lst1=[5,2,2,4,5,4]
lst2=[2,1,5,5,5,1] 
srednjaVrijednost(lst1,lst2)
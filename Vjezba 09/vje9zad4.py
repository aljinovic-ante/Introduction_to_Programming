def djeljivi(lst1,lst2):
    for i in range(len(lst1)):
        if lst1[i]%3==0 and lst1[i] in lst2:
            print(lst1[i])


lst1=[6,4,5,7,2,9,1,3]
lst2=[2,5,1,3,7,8,9]
djeljivi(lst1,lst2)
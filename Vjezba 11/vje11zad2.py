list=[]
brojac = 0
suma = 0
while True:
    broj=int(input("Unesite Broj: "))
    if (broj != 0):
        list.append(broj)
        brojac +=1
    elif broj==0:
       n=int(input("Unesite broj N: "))
       if(len(list) < n ):
           print("Error")
           break
       else:
           zbroj=brojac-n
           for i in range (n):
               suma=suma+list[zbroj]
               zbroj +=1
           break
if 0<n and n<4:
    print("Zbroj zadnjih",n,"broja je",suma)       
else:
    print("Zbroj zadnjih",n,"brojeva je",suma)  

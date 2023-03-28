def parniIndeksi(list):
    for i in range(len(list)):
        if i%2==0:
            print(list[i])
          
def parniElementi(list):
    for i in list:
        if i%2==0:
            print(i)
    
    
list=[3,2,9,5,8,4,7]
print("Parni indeksi: ")
parniIndeksi(list)
print("Parni elementi: ")
parniElementi(list)

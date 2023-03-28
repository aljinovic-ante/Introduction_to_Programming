
list=[]

while True:
    string=input("Unesite: ")
    if string==".":
        break
    list.append(string)
    
for i in list:
    if len(i) > 5:
        print(i)
    
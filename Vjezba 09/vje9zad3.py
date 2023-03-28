def jednake(list):
    flagIsti=True
    flagDvi=True
    brojac=0
    prvi=list[0]
    for e in list:
        if e!=prvi:
            flagIsti=False
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]==list[j] and i!=j:
                brojac=brojac+1
    if brojac<1:
        flagDvi=False
    return flagIsti, flagDvi

list=[6,5,2,7,6,8,3]
print(jednake(list))
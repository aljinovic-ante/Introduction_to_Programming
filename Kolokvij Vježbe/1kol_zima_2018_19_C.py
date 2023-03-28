#Napisati program koji od korisnika čita dva po dva broja. Program za
#svaka dva broja ispisuje sve brojeve između njih.

while True:
    a=int(input("broj: "))
    b=int(input("broj: "))
    for i in range(a+1,b):
        print(i)
n=int(input("unesi broj"))

for x in range(n):
    for y in range(n):
        if(y==0 or y==n-1 or x==n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")
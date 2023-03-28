N=int(input("Unesite broj: "))
for r in range(N):
    for s in range(N-2):
        if r==0 or r==N//2 or r==N-1 or s==N-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
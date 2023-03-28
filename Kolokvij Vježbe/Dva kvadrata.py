N=int(input("Unesite stranicu kvadrata: "))

"""r=red, s=stupac"""
"""
   *****
   *   *
   *   *
   *   *
   *********
       *   *
       *   *
       *   *  
       *****  """
       
x=2*N-1
for r in range(x):
    for s in range(x):
        if r==0 and s in range (0, x//2) or r==x//2 or s==x//2 or s==x-1 and r in range(x//2,x) or r==x-1 and s in range (x//2,x) or r in range (0, x//2) and s==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

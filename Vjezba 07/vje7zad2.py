def pom_funk(broj):
    zbroj = 0
    for i in range (2,broj+1):
        if broj%i==0:
            zbroj+=i
    if zbroj==broj:
        return True
    else:
        return False

def funk(n):
    for i in range(1,n):
        if pom_funk(i) and n%i==0:
            print(i)
            
funk(200)
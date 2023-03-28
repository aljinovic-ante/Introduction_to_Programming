def pom_funk(i,n):
    if n%i==0:
        return True
    else:
        return False
    
def funk(n):
    broj=0
    for i in range(1,n+1):
        if pom_funk(i,n):
            broj+=1
            
    return(broj)
    
print(funk(15))
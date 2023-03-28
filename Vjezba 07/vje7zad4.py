def funk(n):
    if n==0:
        return 0
    if n%2!=0:
        n-=1
    if n%2==0:
        print(n)
        return n + funk(n-2)
    
x = funk(15)
print(x)
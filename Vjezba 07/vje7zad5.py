def funk(n):
    if n==0:
        return 0
    
    funk(n//2)
    print(n%2, end="")
    
funk(150)
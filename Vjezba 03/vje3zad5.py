a=9
b=3

#a
if a>0 and b>0:
    print("True")
else:
    print("False")
    
#b
if a%2==0 and b%2==0:
    print("True")
else:
    print("False")
    
#c
if a%b==0 and b%2==0 and a>b:
    print("True")
else:
    print("False")
    
#d
if a%2==1 or b%2==1:
    print("True")
else:
    print("False")
    
#e
if a%2==0 and b%2==1 or a%2==1 and b%2==0:
    print("True")
else:
    print("False")
    
#f
if a%b==0 or b%a==0:
    print("True")
else:
    print("False")
    
#g
if a%b==0 and b%a!=0:
    print("True")
else:
    print("False")
    

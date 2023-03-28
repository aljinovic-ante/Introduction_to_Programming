#a
ip=3292799233
if(((ip>>24&255)==196) and ((ip>>16&255)==68)):
    print("True")
else:
    print("False")
#b
ip=3292799233
if((ip&255)<128 and (ip>>8&255)<128 ):
    print("True")
else:
    print("False")
#c
a=3292799233
if(ip>>24&255 == ip&255):
    print("True")
else:
    print("False")
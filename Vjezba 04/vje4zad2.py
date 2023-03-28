a=69
b=13
#a
if(a&1==1):
    print("true")
else:
    print("false")
#b
if(a>>3&1==1):
    print("true")
else:
    print("false")
#c
if(a&7 == b&7):
    print("true")
else:
    print("false")
#d
if(a>>1&7 == b>>1&7):
    print("true")
else:
    print("false")
#e
if(a>>3&1 and a>>5&1):
    print("true")
else:
    print("false")
#f
if(a>>3&1 or a>>5&1):
    print("true")
else:
    print("false")
#g
if(a>>3&1==1 and a>>5!=1)or(a>>5&1==1 and a>>3!=1):
    print("true")
else:
    print("false")
   
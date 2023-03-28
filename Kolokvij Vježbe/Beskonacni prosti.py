import time
def prost(i):
    if i == 1 or i==2:
        return True
    else:
        for a in range (2,i):
            if i%a==0:
                return False
    return True
 
i=1       
while True:
    if prost(i):
        print(i)
        time.sleep(1)
    i=i+1
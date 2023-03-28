"""
1kol_zima_2018_19_B
"""
# Bz1.py
isfinished = False
high = 0
while isfinished != True:
    num = int(input("num?: "))
    if num > high:
        high = num
    else:
        isfinished = True

# Bz2.py
isfinished = False
previous = 0
isfirstrun = True
while isfinished != True:
    num = int(input("num?: "))
    if isfirstrun == True:
        previous = num - 1
        isfirstrun = False
    if (previous % 2) != (num % 2):
        previous = num
    else:
        isfinished = True

# Bz3.py
def isprime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
j = 0
while True:
    if isprime(j):
        print(j)
    j += 1

# Bz4.py
def highcoord(coordA, coordB):
    a, b = coordA
    c, d = coordB
    if (a < 0) or (b < 0):
        return False
    if (c < 0) or (d < 0):
        return False
    if (a + b) > (c + d):
        return coordA
    else:
        return coordB
print(highcoord((1, 2), (3, 4)))
print(highcoord((90, 10), (70, 5)))
print(highcoord((120, -90), (50, 5)))
print(highcoord((99, 1), (99, 1)))
print(highcoord((99, 8), (88, 5)))
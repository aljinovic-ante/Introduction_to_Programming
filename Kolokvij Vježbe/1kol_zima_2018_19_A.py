"""
1kol_zima_2018_19_A
"""

# Az1.py
# *
# **
# *-*
# *--*
# *---*
# ******

n = int(input("n?: "))
print("*")
for i in range(0, n - 2):
    print("*" + "-" * i + "*")
print("*" * n)

# Az2.py
def maxdiff(a, b, c):
    high = 0
    if a > b and a > c:
        high = a
    elif b > a and b > c:
        high = b
    else:
        high = c
    low = 0
    if a < b and a < c:
        low = a
    elif b < a and b < c:
        low = b
    else:
        low = c
    return (high-low)
print(maxdiff(150, 50 ,75))

# Az3.py
def readnumbers():
    isfinished = False
    while isfinished != True:
        a = int(input("a?: "))
        b = int(input("b?: "))
        c = int(input("c?: "))
        if a == 0 and b != 0 and c != 0:
            if b % 2 == 0 and c % 2 == 0:
                isfinished = True
        elif b == 0 and a != 0 and c != 0:
            if a % 2 == 0 and c % 2 == 0:
                isfinished = True
        elif c == 0 and a != 0 and b != 0:
            if a % 2 == 0 and b % 2 == 0:
                isfinished = True
    return (a, b, c)
print("Enter two even and one zero in any order to quit.")
retval = readnumbers()
print(retval)


# Az4.py
def skrati(brojnik, nazivnik):
    high = 0
    if brojnik > nazivnik:
        high = brojnik
    else:
        high = nazivnik
    maxdivisor = 0
    for i in range(1, high + 1):
        if brojnik % i == 0 and nazivnik % i == 0:
            maxdivisor = i
    brojnik = brojnik // maxdivisor
    nazivnik = nazivnik // maxdivisor
    print("max divisor:" + str(maxdivisor))
    return (brojnik, nazivnik)
print(skrati(120, 60))
print(skrati(81, 9))
print(skrati(220, 80))
print(skrati(99, 33))
print(skrati(50, 5))
print(skrati(78, 3))
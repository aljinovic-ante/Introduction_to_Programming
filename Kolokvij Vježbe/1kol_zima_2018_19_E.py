"""
1kol_zima_2018_19_E
"""

"""
# Ez1.py
while True:
    a = int(input("a?: "))
    b = int(input("b?: "))
    if a < b:
        for i in range(a + 1, b):
            print(i)
    else:
        for i in range(a - 1, b, -1):
            print(i)
"""
# Ez2.py
counter = 0
while True:
    num = int(input("num?: "))
    if num > 0:
        counter += 1
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)
    elif num < 0:
        continue
    elif num == 0:
        print("End.")
        break
    if counter == 10:
        break

# Ez3.py
def fun():
    isfirstrun = True
    preva = 0
    prevb = 0
    while True:
        a = int(input("a?: "))
        b = int(input("b?: "))
        if isfirstrun:
            preva = a + 1
            prevb = b + 1
            isfirstrun = False
        if a > preva and b > prevb:
            return (a, b)
        preva = a
        prevb = b
retval = fun()
print(retval)

# Ez4.py
def digitsum(number):
    while number > 0:
        return number % 10 + digitsum(number//10)
    return 0
print(digitsum(25678939), "=?", 2+5+6+7+8+9+3+9)


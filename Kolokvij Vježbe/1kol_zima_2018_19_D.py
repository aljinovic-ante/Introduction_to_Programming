"""
1kol_zima_2018_19_D
"""
# Dz1.py
isfinished = False
sum = 0
while isfinished != True:
    num = int(input("num?: "))
    if num > sum:
        sum += num
    else:
        isfinished = True

# Dz2.py
for i in range(1, 1001):
    if i % 3 == 0 and i % 5 != 0:
        print(i, "fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print(i, "buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(i, "fizzbuzz")
    else:
        print(i)

# Dz3.py
def fun():
    print("Enter two positive numbers to stop.")
    while True:
        a = int(input("a?: "))
        b = int(input("b?: "))
        if a > 0 and b > 0:
            return (a, b)
fun()

# Dz4.py
# nesto mi je odi sumnjivo
def countones(number):
    ones = 0
    while number > 0:
        ones = ones + number&1
        return ones + countones(number>>1)
    return 0
for i in range(0, 256):
    print(i, bin(i), countones(i))

    
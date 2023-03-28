"""
1kol_zima_2018_19_F
"""

"""
# Fz1.py
isfirstrun = True
prev = 0
while True:
    num = int(input("num?: "))
    if isfirstrun == True:
        prev = num
        isfirstrun = False
        continue
    print(prev - num)
    prev = num
"""

# Fz2.py
# 1kol_zima_2018_19_B.pdf ---> z4

# Fz3.py
def fun(number):
    first = 0
    last = 0
    first = number % 10
    while number > 0:
        last = number % 10
        number //= 10
    return (first == last)
print(fun(1234567891))
print(fun(987654321))

# Fz4.py
# 1kol_zima_2018_19_E.pdf ---> z4


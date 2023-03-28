import string
slova = string.ascii_uppercase
d = dict(zip(slova, "22233344455566677778889999"))

phone = "555-CALL-ME".upper()

for k,v in d.items():
    phone=phone.replace(k, str(v))

print(phone)
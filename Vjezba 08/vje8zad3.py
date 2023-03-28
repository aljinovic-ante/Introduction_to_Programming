def razlika(a,b):
    if (a==0 and b==0):
        return 0
    if (a%10 != b%10):
        return 1 + razlika(a//10,b//10)
    else:
        return 0 + razlika(a//10,b//10)
    
print(razlika(36415,32816))
    
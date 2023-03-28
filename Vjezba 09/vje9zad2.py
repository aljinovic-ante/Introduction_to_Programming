def rastuciNiz(list):
    for i in range(len(list)):
        if list[i]<list[i-1] and i != 0:
            return False
    return True


list=[1,2,6,3,5,4,7]
print(rastuciNiz(list))
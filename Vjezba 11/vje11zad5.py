def funkcija():
    rjecnik = {'Petar':54,'Josip':47,'Marko':84}
    total = sum(rjecnik.values())
    novi={key:("{:.1%}".format(val/total)) for key,val in rjecnik.items()}
    print(novi)

funkcija()
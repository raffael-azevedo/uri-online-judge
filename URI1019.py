segundos = int(input(""))

horas = int((segundos/60)/60)
minutos = int((segundos/60) - (horas * 60))
segundos = int(segundos - ((horas*60*60) + (minutos * 60)))

print(str(horas)+":"+str(minutos)+":"+str(segundos))

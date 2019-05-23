idade = int(input(""))

anos = int(idade/365)
meses = int(idade%365)/30
dias = int(idade%365%30)

print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(anos, meses, dias))

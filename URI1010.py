line1 = input().split(" ")
line2 = input().split(" ")

prod1, units1, valor1 = line1
prod2, units2, valor2 = line2

total = (int(units1) * float(valor1)) + (int(units2) * float(valor2))
print("VALOR A PAGAR: R$ %0.2f" %total)

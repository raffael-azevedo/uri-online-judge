line = input().split(" ")

code, quant = line

code = int(code)
quant = int(quant)

if(code == 1):
	price = 4.00
elif(code == 2):
	price = 4.50
elif(code == 3):
	price = 5.00
elif(code == 4):
	price = 2.00
elif(code == 5):
	price = 1.50

total = price * quant
print("Total: R$ %.2f" %total)

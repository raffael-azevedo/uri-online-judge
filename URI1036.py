import math
variables = input().split(" ")

a,b,c = variables
a = float(a)
b = float(b)
c = float(c)

delta = (b ** 2) - (4 * a * c)
r1 = (-b+(math.sqrt(delta)))/(2*a)
r2 = -b - (math.sqrt(delta))/(2*a)

if(math.sqrt(delta) < 0 or float(a) == 0):
    print("Impossivel calcular")
else:
    print("R1 = %.5f" %r1)
    print("R2 = %5.f" %r2)

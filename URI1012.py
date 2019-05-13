line1 = input().split(" ")

A, B, C = line1

triangle = (float(A)*float(C))/2
circle = 3.14159 * (float(C) ** 2)
trapezium = (float(A) + float(B))/2 * float(C)
square = float(B) ** 2
rectangle = float(A) * float(B)

print("TRIANGULO: %0.3f" %triangle)
print("CIRCULO: %0.3f" %circle)
print("TRAPEZIO: %0.3f" %trapezium)
print("QUADRADO: %0.3f" %square)
print("RETANGULO: %0.3f" %rectangle)

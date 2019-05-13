import math
line1 = input().split(" ")
line2 = input().split(" ")

x1, y1 = line1
x2, y2 = line2

distance = math.sqrt(((float(x2)-float(x1)) ** 2) + ((float(y2)-float(y1)) ** 2))
print("%0.4f" %distance)

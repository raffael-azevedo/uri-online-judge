line1 = input().split(" ")
A, B, C = line1

maiorAB = (int(A)+int(B)+abs(int(A)-int(B)))/2
maiorABC = (maiorAB+int(C)+abs(maiorAB-int(C)))/2

print("%d eh o maior" %maiorABC)

adad = input().split()
n = int(input())
suma=0
for i in range(len(adad)):
    if i<n:
        suma+=int(adad[i])
print(suma)
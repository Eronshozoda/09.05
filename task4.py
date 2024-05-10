my_list = input().split()
suma=0
for i in my_list:
    if int(i)>int(5):
        suma+=int(i)
print(suma)
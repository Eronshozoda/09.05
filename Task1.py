def summa(a):
    if a==1:
        return 1
    res = a+summa(a-1)
    return res
a = int(input())
print(summa(a))
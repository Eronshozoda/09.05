def jam(a):
    if len(a)==0:
        return 0
    else:
        return a[0] + jam(a[1:])
print(jam([1, 2, 3, 4, 5]))
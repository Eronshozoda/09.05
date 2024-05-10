numbers = input().split()
numbers.sort()
for i in numbers:
    if int(i)%2!=0:
        print(i)
        break
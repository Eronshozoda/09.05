list1 = input()
cnt=0
for i in range(len(list1)):
    if list1[i:i+6]=="potato":
        cnt+=1
print(cnt)
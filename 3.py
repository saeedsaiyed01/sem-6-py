#multiplication table printer

num=int(input())

for i in range(1,11):
    if i == 5:
        continue
    print(num,"x",i,"=",num*i)
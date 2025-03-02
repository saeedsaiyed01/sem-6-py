#Write a Python program to implement Factorial series up to user entered number.

num=int(input("Enter Number:"))
fact=1
for i in range(1,num+1):
    fact=i*fact

print(fact)

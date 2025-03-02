#Write a Python program to calculate sum of given number.

number=int(input("Enter Number: "))
sum=0
for i in range(1,number+1):
    sum=sum+i

print(sum)


# n=int(input("Enter Number: "))
# sum=0

# while(n>0):
#     r=n%10
#     sum=sum+r
#     n=n//10

# print("Sum of digits of entered numbers is ",sum)

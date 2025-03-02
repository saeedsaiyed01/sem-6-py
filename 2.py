# sum of even number

nums= int(input())
sum_even=0

for num in range(1,nums+1):
    if num%2==0:
        sum_even +=1


print("Sum of even number is:",sum_even)




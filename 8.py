

nums=int(input("Enter Number:  "))

is_prime=True

if nums>1:
    for num in range(nums):
        if nums%2==0:
            is_prime=False
            break

print(is_prime)

#if number is not divide its true = means = its prime number
#if it is divisiable its means it non prime number like 10 ,14 etc.
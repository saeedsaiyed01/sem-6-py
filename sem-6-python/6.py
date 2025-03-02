#6. Write a Python Program to Check Armstrong Number
def is_armstrong_number (num):
    num_str=str(num)

    num_digits=len(num_str)

    sum_of_power=0

    for digit in num_str:
        sum_of_power= sum_of_power+int(digit) ** num_digits

    return sum_of_power==num    
number=153
if is_armstrong_number(number):
    print( f'{number} It is Armstrong Number')
else:
    print(f'{number} Not Armstrong Number.')
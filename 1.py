# prime number in python 
nums =[1,-2,-3,4,5,6,-6,-7,8,9,10]

positive_number_count=0

for num in nums:
    if num > 0:
        positive_number_count += 1

print("Final count of positive number is",positive_number_count)
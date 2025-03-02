#11 . Write a python program to display ascending and descending order from given 10 
#numbers
numbers = list(map(int, input("Enter 10 numbers separated by space: ").split()))
if len(numbers) !=10:
    print("Error: Please enter exactly 10 numbers..")

else:

    ascending_order= sorted(numbers)    

    descending_order = sorted(numbers, reverse=True)

    print("Ascending order:", ascending_order)
    print("Descending order:", descending_order)
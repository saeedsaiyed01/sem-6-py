# # Write a Python program to display the Fibonacci series

# try:
#     num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    
#     if num_terms <= 0:
#         print("Please enter a positive integer.")
#     else:
#         a = 0
#         b = 1
#         print("Fibonacci series:")
        
#         for i in range(num_terms):
#             print(a, end=" ")
#             a, b = b, a + b
        
#         print()  # For a newline after printing the series

# except ValueError:
#     print("Invalid input. Please enter a valid integer.")




x=0;
y=1
z=0

print("first 25 terms of fibonacci series")

count=1

while(count<=25):
    print(z,end=" ")
    x=y
    y=z
    z=x+y
    count=count+1
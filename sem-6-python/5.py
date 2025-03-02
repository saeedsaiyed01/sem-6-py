number = int(input("Enter a number: "))
#100
for num in range(2, number + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    #print
    if prime:
        print(num, end=" ")

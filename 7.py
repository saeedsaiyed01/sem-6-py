#validate input

while True:
    number = int(input("Enter value b/w 1 to 10: "))
    if 1<=number <=10:
        print('Thanks')
        break

    else:
        print("Invaild number,try again ")
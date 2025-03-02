#22. Write a Python program for Error Handling. 


try:
    a=[11,22,33]
    print(a[4])
    try:
        a=10/0
        print(a)

        d={1:"BCA",2:"MCA"}
        print(d[1])
    except KeyError:
        print("Key Error")

except ZeroDivisionError:
    print("This is statement is raising an arithmetic exeption")

except IndexError:
    print("Index out of Bound Error")

else: 
    print("BCA COLLEGE:")

finally:
    print("")
    print("THIS WILL EXECUTE ALWAYS!")
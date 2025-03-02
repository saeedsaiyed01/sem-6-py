#21. Write a Python program to read a file bca.txt and print the contents of file along 
#with number of vowels present in it. 


f = open("C:/Users/Saeed/OneDrive/Desktop/python/sem-6-python/bca.txt", "r")
total=0

vowels=["a","e","i","o","u","A","E","I","O","U"]
print("Content of the file are \n")

for i in f.read():
    print(i,end="")
    if i in vowels:
        total=total+1

print(" Total vowels are:")
print(total)
f.close()
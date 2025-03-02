#Write a Python program to print the duplicate elements of an array


import array as arr

a =arr.array('i',[1,2,3,4,4])
b=[""]
print(a)

for i in a:
    if a.count(i) == 2:
     print(i)
     break




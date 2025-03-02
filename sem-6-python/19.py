#19. Write a Python program to create nested list and display its elements. 

l=["a","b",["c","d",["eee","fff"]],"g","h"]

print(l)
print("Display all Element")

for i in range(len(l)):
    print(l[i])


print("Display particular element")

print(l[1])
print(l[2])
print(l[3])
print(l[2][2])
print(l[2][2][1])
print(l[2][0])




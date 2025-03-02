#18.Write Python programs to implement a concept of tuples.

#tuple

x=(10,20,"bca","college")
print(x)
print(x[2])
print(x[-1])

#slicing

print(x[0:2])
print(x[1:3])
print(x[-4:-1])

y=("Palanpur",66,77)
c=x+y
print(c)
print(c*2)

#convert into list
a=list(x)
print(type(a))

a[1]=55 #modify
print(a)

#insert operation

a.append("deesa")
a.insert(2,"bba")

x=tuple(a)
print(type(x))
print(x)

#deletion

a=list(x)
a.pop()
a.remove(55)
x=tuple(a)
print(x)

#display each element for loop:

for i in x:
    print(i)


#while loop
print()
print("while loop")

i=0
while i<len(x):
    print(x[i])
    i=i+1
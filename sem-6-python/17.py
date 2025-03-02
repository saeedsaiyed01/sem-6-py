#17.  Write Python programs to implement a concept of list.

#list

a=[12,24,34]
b=[11,22,33,44]


print(a)
print(b)
print(b[-1])

print("Concatation Operation")
print(a+b)

print("Repeatation Operation")
print(a*3)
print(type(b))

print("Slicing Operation")
print(a[2:5])

print(a[-4:-1])
print(b[1:6])



s1=["bca college",10,"palanpur"]
print(s1)
print(type(s1))

print("Modify Operation")
s1[1]=20

print(s1)

print("Insert Operation")
s1.append("xyz")
print(s1)

s1.insert(2,"python")
print(s1)

print("Pop Operation")
s1.pop(4)
print(s1)

print("Remove Operation")
s1.remove(20)
print(s1)

print("Sorting")
s1.sort()
print(s1)


#display each element

for i in s1:
    print(i)

print("------")
for i in range(len(s1)):
    print(s1[i])

#without list comprehension 

fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print("With List comprehension ")
#with list comprehension 
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

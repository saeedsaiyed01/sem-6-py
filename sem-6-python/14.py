#14.  Write Python programs to using lambda function. 

a= int(input("Enter Args1"))
b= int(input("Enter Args2"))

op=input("Enter Operator")

if op=="+":
    sum= lambda x,y:x+y
    print("Value of Total=> " ,sum(a,b))

elif op=='-':
    sub = lambda x,y:x-y
    print("Value Of Total=> ",sub(a,b))

elif op=='*':
    mul=lambda x,y:x*y
    print("Value Of Total+> ",mul(a,b))

elif op=='/':
    div=lambda x,y:x/y
    print("Value Of Total+> ",div(a,b))

else:
    print("Invalid Operator")
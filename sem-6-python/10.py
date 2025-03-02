# write a py program to check number is palindrome or not

n=int(input("Enter Number"))

number=n;
rnumber=0;2

while(n>0):
    digit=n%10
    rnumber=(rnumber*10)+digit
    n=n//10

if number ==rnumber:
  
  print("Palindrome")

else:
   print("Not palindrome")
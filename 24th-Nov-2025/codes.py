### \#simple calculator

a= int(input("Enter first number"))

b = int(input("Enter second number"))

print("Sum:",a+b)

print("Difference:",a-b)

print("Product:",a\*b)

print("division:",a/b)



### \#Age in 2050

birth\_year= int(input("Enter your birth year:"))

age\_in\_2050 = 2050 - birth\_year

print("You will be ", age\_in\_2050,"years old in 2050")

\#Area of a Rectangle

l = int(input(" length:"))

b= int(input("breadth: "))

print("Area:",l\*b)



### \#Area of a Rectangle

l = int(input(" length:"))

b= int(input("breadth: "))

print("Area:",l\*b)



### \#Even or Odd



num = int(input("Enter a number: "))



if num % 2 == 0:

&nbsp;   print(f"{num} is Even")

else:

&nbsp;   print(f"{num} is Odd")



### \#Simple Login Check



username = input("Enter username: ")

password = input("Enter password: ")

if username == "admin" and password == "1234":

&nbsp;   print("Login Successful")

else:

&nbsp;   print("Invalid Login")



### \#Square \& Cube of a Number

number = int(input(" enter a number :"))

square = num \*\* 2

cube = num \*\* 3

print(f"Square of {num} is {square}")

print(f"Cube of {num} is {cube}")



### \#Convert Minutes to Hours \& remaining minutes



total\_minutes = int(input("Enter total minutes: "))

hours = total\_minutes // 60

remaining\_minutes = total\_minutes % 60

print(hours)

print(minutes)



### \#Swap Two Variables

a=int(input("Enter the first number:"))

b= int(input("Enter the second number:"))

a,b=b,a

print("After Swapping:")

print("a=",a)

print("b=",b)



### \#Check Positive, Negative,or Zero

num = int(input("Enter a Number:"))

if num > 0:

&nbsp;   print("positive")

elif num < 0:

&nbsp;   print(" negative")

else:

&nbsp;   print("zero")

&nbsp;   

### \# Find the Last Digit of a number



num = int(input("Enter a number: "))

last\_digit = abs(num) % 10  

print(last\_digit)





### \#Sum of First N Natural Numbers

n = int(input("Enter the value of n :"))

total = 0

for i in range (1,n+1):

&nbsp;   total+=i

print (total)



### \#Multiplication Table



num = int(input("Enter a number: "))

print(f"Multiplication Table for {num}:")

for i in range(1, 11):

&nbsp;   print(f"{num} x {i} = {num \* i}")



### \## Count digits

num = int(input("Enter a number: "))

count = len(str(abs(num))) 

print(count)



### \#Reverse a Number



m = int(input("Enter a number: "))

reverse = 0

while num != 0:

&nbsp;   digit = num % 10           

&nbsp;   reverse = reverse \* 10 + digit  

&nbsp;   num = num // 10 

print(reverse)













&nbsp;



&nbsp;   

&nbsp;   

&nbsp;   

&nbsp;   


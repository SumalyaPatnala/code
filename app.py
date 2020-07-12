print('is_palindrome?')
word = input("enter a word:")
def reversingString(word):
    return word[::-1]

rev=reversingString(word)

if word==rev:
    print(f'{word} a palindrome')
else: print(f'{word} not a palindrome')

print('factorial of a given number')
number = int(input("enter a number:"))
result=1
for n in range(1,number+1):
    result*=n

print(f'Factorial :{result}')
print('Largest number in a list')
numbers=[2,3,6,8,2,9,3]
max=0
for i in numbers:
    if i>max:
        max=i

print (max)
print("Challenge")
someList= [1,1,1,1,5]

for i in someList:
    output=''
    for j in range(i):
        output+='X'

    print(output)

print("Calculating items total cost in a shopping cart!")
price=[10,20,30]
total=0
for item in price:
    total+=item
print(f"Total: {total}")
print("the car game")
word= input(">").upper()
car_status=0
while True:
    if word == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print('quit - to exit')
    elif word == 'START':
        if car_status==0:
            print('car started...Ready to go')
            car_status=1
        elif car_status==1:
            print('Car already started')
    elif word == 'STOP':
        if car_status==0:
            print('car is already stopped')
        elif car_status==1:
            print('Car stopped')
            car_status = 0
    elif word == 'QUIT':
        break
    else:
        print("I don't understand that")
    word = input(">").upper()

def change_number(num):
    num+=10
def change_list(num_list):
    num_list.append(20)
num_val=10
print("*********effect of pass by value*********")
print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:", num_val)
print("-----------------------------------------------")
val_list=[5,10,15]
print("*********effect of pass by reference*********")
print("val_list before function call:", val_list)
change_list(val_list)
print("val_list after function call:", val_list)

print("Displaying sum of first n numbers!!")
num=int(input("Enter n"))
def find_sum(num):
    result = 0
    for i in range(1,num+1):
        result+=i
    return result
print(find_sum(num))
print("Displaying square of a number!!")
num=int(input("Enter a number to find its square:"))
def find_square(num):
    result=num**2
    return result
print(find_square(num))
observe1="What's happening!!"
def passport_check(passport_no):
    observe4="actual copied to formal"
    observe5="func. execution starts"
    if(len(passport_no)==8):
        if(passport_no[0]>="A" and passport_no[0]<="Z"):
            status="valid"
        else:
            status="invalid"
    else:
        status= "invalid"
    observe6="func. execution ends"
    return status
observe2="function with formal arg."
observe3="calling with actual arg."
passport_status=passport_check("M9993471")
print("Passport is",passport_status)
#observe1,2,3,4,5,6 are temporary variables used to explain this concept

print("number guessing game!!!")
secret_number=9
guess_count=0
guess_limit= 3
result=''
while guess_count < guess_limit:
    guess = int(input("Guess:"))
    guess_count+=1
    if guess==secret_number:
        result='You Win!!!'
        break
if result=='You Win!!!':
    print(result)
else: print("You lost!!!")

print("Pound to Kilograms and vice versa")
weight=input("Enter your weight:")
units=input("In (L)lbs or (K)kgs:")
to_units=''
if units.upper()=='L':
    weight=int(weight)*0.45
    to_units='kilograms'
elif units=='K' or units=='k':
    weight=int(weight)//0.45
    to_units = 'pounds'
else:
    print("Enter valid value")
print(f"Your weight is {weight} {to_units}.")
print("username length check")
name=input("enter your name:")
if len(name)<3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name can be maximum of 50 characters")
else:
    print("name looks good")

print("using formatting string")
has_good_credit=True
price=1000000
if (has_good_credit):
    print(f"downpayment:{0.1*price}")
else:
    print(f"downpayment::{0.1*price}")

print("To print first n Fibonacci of numbers")
nterms=int(input("enter a number n:"))
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


print("To print first n half Pyramid of numbers")
num1=int(input("enter a number n:"))
for i in range(0,num1+1):
    print(str(i)*i)
print("To find and display maximum of three given numbers")
num1=int(input("enter num 1:"))
num2=int(input("enter num 2:"))
num3=int(input("enter num 3:"))
max=0
nums=(num1,num2,num3)
for n in nums:
    if(n>max):
        max=n
print(max)
print("whether a given year is leap year or not")
year=input("Enter year:")
year=int(year)
if (year%4==0 and year%100!= 0 or year%400==0):
    print("It is a leap year")
else:
    print("Not a leap year")
print("sum of digits of a number")
num=input("Enter a number:")
sum=0
for n in str(num):
    sum+=int(n)
print(sum)

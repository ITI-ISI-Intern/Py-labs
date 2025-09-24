# Lab:
# print Hello world 
print("Hello World!")
# 	- application to take a number in binary form from the user, and print it as a decimal
def isBinary(number):
    for i in number:
        if i not in ("0" , "1"):
            return False
    return True
def converToDecimal():
    while True:
        binary_num = input("Enter a binary number : ")
        if not isBinary(binary_num):
            print("please Enter a valid number")
            continue
        deci_numer = int(binary_num,2)
        print(deci_numer)
        break 
    
# converToDecimal()    
    
# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
def isNumber(number):
    try:
        float(number)
        return True
    except:
        return False
    
def FizzBuzz(number):
    if not isNumber(number):
        print("Invalid Input!")
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz") 
    elif number % 5 == 0:
        print("Buzz") 

# FizzBuzz(15)        
                     
# 	- Ask the user to enter the radius of a circle print its calculated area and circumference
import math
def calcArea():
    try:
        radius = float(input("Enter radius of circle: "))
        if radius <= 0:
            print("Please enter a valid positive number.")
        else:
            area = math.pi * radius ** 2
            circumference = 2 * math.pi * radius
            print(f"Area: {area:.2f}")
            print(f"Circumference: {circumference:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

# calcArea()        

# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

def userData():
    name=input("Enter your name : ")
    
    if not name.isalpha():
        print("Ivalind name Input !")
        return
    
    email=input("Enter your email : ")
    
    if "@" not in email:
        print("Invalind Email Input !")
        return
    
    print(f'The user name is {name}\nThe user email is {email}')
    
# userData() 
   
# 	- Write a program that prints the number of times the substring 'iti' occurs in a string()
def countSubsItI():
    word=input("Enter the word : ")
    count=0
    for i in range(0,len(word)- 2):
        if word[i] == "i" and word[i+1] == "t" and word[i+2] == "i":
            count += 1
    print(f'Tne number of times iti appear in word {word} = {count}')
   

countSubsItI()
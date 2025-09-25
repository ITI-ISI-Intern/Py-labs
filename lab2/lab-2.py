# 1 - Ask the user to enter 5 numbers.
#     Store them, then display them in ascending order and descending order.
def isValidNumbers(numbers):
    if len(numbers) < 5 or len(numbers) > 5:
        raise Exception("please enter only five numbers")
        
    for i in numbers:
        try:
            float(i)  
        except:
            raise Exception(f"The input should be a number\ninvalid input {i}")  
    
    return True    
        
                  
def task1(): 
   numbers = input("Enter five numbers : ").strip().split()
   if isValidNumbers(numbers):
        numbers.sort()
        print('Ascending order : ')
        for i in numbers: 
           print(int(i) ,end=" ")
        print()

        print('Descending order : ')
        numbers.sort(reverse=True)
        for i in numbers:
           print(int(i) ,end=" ")
        print()

# task1()   
   
# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.

def isValidNumber(num):
     try:
         float(num)
         return True
     except:
         return False 
    

def generate_sequence(length,start):
    
    if not isValidNumber(length):
        raise ValueError("Length should be a number")
    if not isValidNumber(start):
        raise ValueError("Start should be a number")
    
    start=int(start)
    length=int(length)
    sequence = []
    for i in range(start , start+length):
        sequence.append(i)
    print("Generated sequence:", *sequence)
    
def task2():
    length = input("Enter the length of seq : ")
    start = input("Enter the start number of sequence : ")
    generate_sequence(length,start)  
    
# task2()      

# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.
def task3():
    numbers = []

    while True:
        user_input = input("Enter a number (or type 'done' to finish): ").strip()

        if user_input.lower() == "done":
            break

        try:
            num = float(user_input) 
            numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a valid number or 'done' to finish.\n")
            continue

    if numbers:
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        print(f"   Results:")
        print(f"   Total  = {total}")
        print(f"   Count  = {count}")
        print(f"   Average= {average}")
    else:
        print("No numbers were entered.")

# task3()

# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.
def removeDuplicates():
    try:
        numbers = set(map(int,input("Enter a list of number : ").split()))
        sorted_numbers=sorted(numbers)
        print("Result : ",*sorted_numbers)
    except:
        raise ValueError("Enter a Valid Numbers")   

# 6 - Ask the user to enter a sentence.
#     Count how many times each word appears in the sentence
#     and display the result.
def countWords():
    sentence = input("Enter a sentence : ")
   
    words= sentence.split()
    wordsDict = {}
    
    for i in words:
        wordsDict[i] = sentence.count(i)
    
    print(wordsDict)

# countWords()

# 7 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.
def gradeBookSystem():
    students = {}
    
    try:
        student_nums= int(input("Enter Number of students : "))
    except:
        raise ValueError("Invalid Number input!")
    
    for _ in range(student_nums):
        student_name=input("Enter the student name : ")
        try:
            student_score=int(input("Enter the student scores : ").strip())
        except:
            raise ValueError("student score should  be a number")
        
        students[student_name]=student_score
    
    students_sorted=dict(sorted(students.items(),key=lambda item:item[1]))
    students_list=list(students_sorted.items())
    print(f"The lowset score achieved by {students_list[0][0]}  student : {students_list[0][1]}")
    print(f"The higesht achieved by  {students_list[-1][0]}  student : {students_list[-1][1]}")
    print("The avarage score : ", sum(students_sorted.values())/len(students_sorted))
 
# gradeBookSystem()   
        
# 8 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.

cart = {}    
def add_item():
    name = input("Enter item name: ")
    price_input = input("Enter item price: ")
    try:
        price = float(price_input)
    except ValueError:
        print("Invalid price. Please enter a numerical value.")
        return
    cart[name] = price
    print(f"Added {name} (${price:.2f})")

def remove_item():
    name = input("Enter item name to remove: ")
    if name in cart:
        del cart[name]
        print(f"Removed {name}")
    else:
        print(f"Item '{name}' not found in cart.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("Shopping cart items:")
    for name, price in cart.items():
        print(f"- {name}: ${price:.2f}")

def total_cost():
    total = sum(cart.values())
    print(f"Total cost: ${total:.2f}")

def shoppingCart():
    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. View total cost & exit")
        choice = input("Choose an option (1-4): ")
    
        match choice:
            case '1':
                add_item()
            case '2':
                remove_item()
            case '3':
                view_cart()
            case '4':
                view_cart()
                total_cost()
                print("Thank you for shopping!")
                break
            case _:
                print("Invalid option. Please try again.")


    

# 9 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts.
import random

def calculate_score(attempts):
    score = max(100 - (attempts - 1) * 5, 10) 
    return score

def guessGame():
    secret_number = random.randint(1, 20)
    attempts = 0

    print(" Number Guessing Game!")
    print("Guess a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations!")
                print(f"The Guesed number was {secret_number}")
                print(f"It took you {attempts} attempts.")
                print(f"your score is : {calculate_score(attempts)}")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
        except ValueError:
            print("Please enter a valid number.")


while True:
        print("Python Practice Tasks")
        print(" ")
        print("1: List in Asc and Desc")
        print("2: Sequence")
        print("3: Numbers calculations")
        print("4: Remove duplicates and sort")
        print("5: Count words in sentence")
        print("6: Gradebook")
        print("7: Shopping cart")
        print("8: Guess secret")
        print("0: Quit")
        
        choice=input("Enter your choice : ").strip()
        match choice:
            case '1':
                try:
                 task1()
                except Exception as e:
                    print(e)
                    task1()
            case '2':
                try:
                    task2()
                except Exception as e:
                    print(e)
                    task2()
            case '3':
                try:        
                    task3()
                except Exception as e:
                    print(e)
                    task3()
            case '4':
                try:
                    removeDuplicates()
                except Exception as e:             
                    print(e)
                    removeDuplicates()
            case '5':       
                try:
                    countWords()
                except Exception as e:             
                    print(e)
                    countWords()
            case '6':       
                try:
                    gradeBookSystem()
                except Exception as e:           
                    print(e)
                    gradeBookSystem()
            case '7':
                try:
                    shoppingCart()
                except Exception as e:           
                    print(e)
                    shoppingCart()
            case '8':
                try:
                    guessGame()
                except Exception as e:           
                    print(e)
                    guessGame()
            case '0':
                print("Exiting the program. Goodbye!")
                break

        input("Press Enter to continue...")

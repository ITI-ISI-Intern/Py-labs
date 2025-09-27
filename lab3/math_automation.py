import os
import math

from decorator_task import log_time
"""
1) Math Automation
   - Create a file called "math_report.txt".
   - Ask the user for multiple numbers (comma-separated).
   - For each number, calculate:
        - floor, ceil, square root, area of a circle
   - Write the results into "math_report.txt".
   - Confirm file was created and print its content.
   
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@log_time
def mathAutomation():
    while True:
        # make validation 
        try:
            user_input = input("Enter multiple numbers separated by commas: ").strip()
            if not user_input:
                print("Error: Please enter at least one number.")
                continue
            
            numbers = [float(x.strip()) for x in user_input.split(',')]
            break
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers separated by commas.")
    
    # writing to file 
    file_path = os.path.join(BASE_DIR, "files/math_report.txt")
    with open(file_path, "w") as file:
        for number in numbers:
            floor_value = math.floor(number)
            ceil_value = math.ceil(number)
            sqrt_value = math.sqrt(number) if number >= 0 else "undefined"
            area_circle = math.pi * (number ** 2)

            file.write(f"Number: {number}\n")
            file.write(f"  Floor: {floor_value}\n")
            file.write(f"  Ceil: {ceil_value}\n")
            file.write(f"  Square Root: {sqrt_value}\n")
            file.write(f"  Area of Circle: {area_circle}\n")
            file.write("\n")

    if os.path.exists(file_path):
        print(f"{file_path} has been created. Here are its contents:\n")
        with open(file_path, "r") as file:
            print(file.read())
    else:
        print("Failed to create the file.")

# mathAutomation()
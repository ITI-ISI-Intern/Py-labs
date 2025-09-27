#!/usr/bin/env python3

def display_menu():
    """Display the main menu with all available tasks"""
    print("\n" + "="*60)
    print("           PYTHON AUTOMATION TASKS MENU")
    print("1. Math Automation")
    print("2. Regex Log Cleaner")
    print("3. Datetime Reminder Script")
    print("4. Product Data Transformer")
    print("5. OS File Manager")
    print("6. Random Data Generator")
    print("7. Exit")

from date_reminder import dateReminder
from math_automation import mathAutomation
from file_manager import fileManager
from math_automation import mathAutomation
from product_transformer import productDataTransformer
from random_number_genrator import randomGenerator
from regx_validation import regexLogCleaner

def run_task(choice):

    match choice:
        case 1:
            task_name, task_function = "Math Automation", mathAutomation
        case 2:
            task_name, task_function = "Regex Log Cleaner", regexLogCleaner
        case 3:
            task_name, task_function = "Datetime Reminder Script", dateReminder
        case 4:
            task_name, task_function = "Product Data Transformer", productDataTransformer
        case 5:
            task_name, task_function = "OS File Manager", fileManager
        case 6:
            task_name, task_function = "Random Data Generator", randomGenerator
        case 7:
            print("\nThank you for using Python Automation Tasks!")
            return False
        case _:
            print("Invalid choice. Please try again.")
            return True

    print(f"\nRunning: {task_name}")
    
    try:
        result = task_function()
        print(f"\nTask completed successfully: {result}")
    except KeyboardInterrupt:
        print(f"\nTask '{task_name}' was interrupted by user.")
    except Exception as e:
        print(f"\nError in '{task_name}': {e}")
    
    input("\nPress Enter to return to menu...")
    return True


if __name__ == "__main__":
    while True:
        display_menu()
        try:
            choice = int(input("Select a task (1-7): "))
        except ValueError:
            print("Please enter a valid number between 1 and 7.")
            continue
        if not run_task(choice):
            break

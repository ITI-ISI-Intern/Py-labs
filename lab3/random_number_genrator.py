import csv
import os
import random

from decorator_task import log_time  


'''
Random Data Generator
   - Ask user how many random numbers to generate.
   - Save them into "random_numbers.csv" as:
        index,value
        1, 42
        2, 87
        ...
   - Print total count and average of the generated numbers. 
'''

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@log_time
def randomGenerator():
    while True:
        try:
            count_input = input("How many random numbers to generate? ").strip()
            
            if not count_input:
                print("Error: Please enter a number.")
                continue
            
            count = int(count_input)
            
            if count <= 0:
                print("Error: Please enter a positive number.")
                continue
            
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    random_numbers = [random.randint(1, 1000) for _ in range(count)]   


    os.makedirs(os.path.join(BASE_DIR, "files"), exist_ok=True)
    file_path = os.path.join(BASE_DIR, 'files/random_numbers.csv')
    
    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["index", "value"])
        for i, value in enumerate(random_numbers, 1):
            writer.writerow([i, value])

    total_count = len(random_numbers)
    average = sum(random_numbers) / total_count
    
    print(f"\nGenerated {total_count} random numbers")
    print(f"Average value: {average:.2f}")
    print(f"Random numbers saved to '{file_path}'")
    
    preview_count = min(5, total_count)
    print(f"\nPreview of first {preview_count} numbers:")
    for i in range(preview_count):
        print(f"  {i+1}: {random_numbers[i]}")
    
    return f"Generated {total_count} random numbers with average {average:.2f}"

# randomGenerator()

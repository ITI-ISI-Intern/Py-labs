'''
7) Decorators Task
   - Create a decorator called "log_time" that:
        - Records the execution time of any function.
        - Saves the function name and runtime into "execution_log.txt".
   - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
   - Verify that the log file contains entries after running.
'''

import time
import os
from functools import wraps

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'files/execution_log.txt')

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        LOG_FILE_PATH = os.path.join(BASE_DIR, 'files/execution_log.txt')
        with open(LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f"{func.__name__}: {execution_time:.4f} seconds\n")
            
        return result
    
    return wrapper
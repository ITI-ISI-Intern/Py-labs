import re
import os

from decorator_task import log_time
"""
Regex Log Cleaner
   - Create a file called "access.log" with 10 fake log lines
     (mix valid emails and invalid strings).
   - Use regex to extract all valid emails.
   - Save them into "valid_emails.txt".
   - Print how many unique emails were found.
"""

BASE_DIR= os.path.dirname(os.path.abspath(__file__))

@log_time
def regexLogCleaner():
    filepath = os.path.join(BASE_DIR, "files/access.log")
    with open(filepath, "r") as file:
        log_data = file.readlines()
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        emails = re.findall(email_pattern, "".join(log_data))

        unique_emails = set(emails)

    # Write valid emails to file
    out_path = os.path.join(BASE_DIR, "files/valid_emails.txt")
    with open(out_path, "w") as file:

        for index,email in enumerate(unique_emails):
            file.write(email + "\n")
            print(f"Email {index + 1}: {email}")
        file.write(f"\nTotal unique valid emails found: {len(unique_emails)}\n")
        print(f"\nTotal unique valid emails found: {len(unique_emails)}")

# regexLogCleaner()
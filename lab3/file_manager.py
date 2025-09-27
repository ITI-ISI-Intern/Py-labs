import os
import shutil


'''
5) OS File Manager
   - Ask user for a directory path.
   - Automatically:
        - Create a folder "backup" inside it if not exists.
        - Copy all .txt files into "backup".
        - Print summary: how many files copied.
   - If directory invalid, retry until correct.

'''

def fileManager():
    # validate input
    while True:
        dir_path = input("Enter a directory path: ")
        if os.path.isdir(dir_path):
            break
        else:
            print("Invalid directory. Please try again.")

    # create backup folder
    backup_dir = os.path.join(dir_path, "backup")
    os.makedirs(backup_dir, exist_ok=True)

    # get all .txt files
    txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt') and os.path.isfile(os.path.join(dir_path, f))]
    
    # copy files to backup
    for file_name in txt_files:
        src_file = os.path.join(dir_path, file_name)
        dest_file = os.path.join(backup_dir, file_name)
        shutil.copy2(src_file, dest_file)

    print(f"Copied {len(txt_files)} .txt files to 'backup' folder.")
     
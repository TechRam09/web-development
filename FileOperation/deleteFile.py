import os

if os.path.exists('Nishu.txt'):
    os.remove('Nishu.txt')
    print("File Deleted")
else:
    print("File does not exist")
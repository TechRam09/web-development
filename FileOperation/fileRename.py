import os
if os.path.exists('Nimbe.txt'):
    os.rename('Nimbe.txt','Shree.txt')
    print("File renamed")
else:
    print("the file does not exist")
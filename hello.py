# print("Hello World")

n = 5

for i in range(1,n):
    for j in range(1,i):
         print('* ',end="")
    for j in range(i,n):
         print(' ',end="")
    for j in range(i,n):
         print(' ',end="")
    for j in range(1,i):
         print('* ',end="")
    print('\n')
    
    
    
for i in range(1,n+1):
    for j in range(i,n):
         print('* ',end="")
    for j in range(1,i):
         print(' ',end="")
    for j in range(1,i):
         print(' ',end="")
    for j in range(i,n):
         print('* ',end="")
    print('\n')
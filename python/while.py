# write a program to print first 10 integers and their squares using while loop

i = 1

while(i>=1):
    print(i , i**2, end ="")
    print()   
    i += 1
    if i > 10:
        break
# 1
# 12
# 123
# 1234
# 12345

n = int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print("\n")



# 54321
# 4321
# 321
# 21
# 1
row = int(input("enter the rows")) 
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")
    # print()

# Prints the value of j without a 
# newline (due to end=""), so the numbers
# are printed on the same line.


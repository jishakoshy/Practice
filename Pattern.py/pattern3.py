# *                 -> 1 
# **                -> 2
# ***               -> 3
# ****              -> 4
# *****             -> 5

n = int(input("enter the no. of columns"))
for row in range(1,n):
    for column in  range(1,row+1):
        print("*" , end = " ")
    print()



# 0 0 0 0 0
# 1 1 1 1
# 2 2 2
# 3 3
# 4

# n = int(input("enter the no. of columns"))
# for star in range(0,n):
#     for column in  range(star,n):
#         print(star, end = " ")
#     print()



# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# n = int(input("enter the no. of columns"))
# for star in range(0,n):
#     for column in  range(star,n):
#         print(star, end = " ")
#     print()
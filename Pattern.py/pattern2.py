#       *
#       *
#       ***
#       *
#       *
#       ******
#       *
#       *
#       *********

n = int(input("enter the number"))

for i in range(1,n+1):
    # print("* \n *")
    print("*")
    print()
    print("*")
    print()
    for j in range(i):
        print((3*i) * "*" , end= " ")
    print()
    
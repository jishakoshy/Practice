# An Armstrong number is a positive integer that is
# equal to the sum of its own digits each raised to the 
# power of the number of digits. For example, 153 is an 
# Armstrong number because 153 = 1^3 + 5^3 + 3^3.

def armstrong(num):
    string = str(num)
    sum = 0
    length = len(string)
    for item in string:
        sum +=item ** length

    return sum == num

num = int(input("enter the number"))
is_armstrong = armstrong(num)

if is_armstrong:
    print(f"{num} is an armstrong")
else:
    print(f"{num} is not an armstrong")



n = int(input("enter thr input"))
n = str(n)
sum = 0
for i in n:
    j = i*i*i
    sum += j

    if sum == n:
        print("its a armstrong")
    else:
        print("it is not a armstrong")    
n = 153
n = "153"
sum = 0

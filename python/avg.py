# how to find average of n numbers

# n = int(input("enter how many number's average to find"))
# total_sum = 0
# for i in range(n):
#     number = float(input("enter the number"))
#     total_sum += number

# avg = total_sum / n
# print("average is :",avg)

# n = input("enter  input")
# if not n.isdigit():
#     print("please enter an integer")

def even():
    n = [12, 4, 5, 7, 9, 10]
    i = 0
    while i < len(n):
        if n[i] % 2 == 0:
            print(n[i])
        i += 1  
even()



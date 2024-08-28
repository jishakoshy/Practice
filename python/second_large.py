# findout the second largest element in the list
list1 = [12,4,75,5,7,8,35,67,99,81,13]

n =len(list1) - 1
largest = None
second_largest = None
for num in list1:
    if num > largest:
        largest = num 
        num += 1
        if num > largest:
            temp = largest
            largest = num
            second_largest = temp
    
    
# list1 = [12, 4, 75, 5, 7, 8, 35, 67, 99, 81, 13]

# largest = second_largest = float('-inf')  # Initialize largest and second_largest to negative infinity

# for num in list1:
#     if num > largest:
#         second_largest = largest 
#         largest = num  
#     elif num > second_largest and num != largest:
#         second_largest = num  

# print("Second largest element in the list is:", second_largest)

    

        
       


    
                  # without using sort() how to find 2nd largest element in list1
def second_large_odd(list1):
    list2 = []
    list3 = []
    for num in list1:
        if (num % 2 !=0):
            list2.append(num)
                                             # x = [5,7,13,15,17,213]
    largest_odd = max(list2)
                                              # print(largest_odd)           
    for odd in list2:
        if odd<largest_odd:
            list3.append(odd)
    print(max(list3)) 

list1 = [5,7,10,219]
second_large_odd(list1)


# the efficient way is:--
def second_large_odd(list1):
    largest_odd = None
    second_largest_odd = None
    
    for num in list1:
        if num % 2 != 0:  
            if largest_odd is None or num > largest_odd:
                second_largest_odd = largest_odd
                largest_odd = num
            elif second_largest_odd is None or num > second_largest_odd:
                second_largest_odd = num   
    return second_largest_odd

list1 = [5, 7, 10, 219]
result = second_large_odd(list1)
print(result)

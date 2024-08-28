# how to findout unique element in a list
list = [ 2,4,5,7,8,2,3,7,8,9,2,3,6]

count = 0
unique = []
for x in list:
    if x not in unique:
        unique.append(x)
print(unique)


    # how to findout least element in a list
# list = [4,7,9,8,2]
# least = list[0]
# large = list[0]
# for x in list:
#     if x < least:
#         least = x
#     elif x > large:
#         large= x
# print("least number is:",least)
# print("large number is:",large)

   
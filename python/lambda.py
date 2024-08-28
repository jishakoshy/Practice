# lambda function to return last element in a list

lambda_function = lambda lst : lst[-1]

list = [3,5,7,5,2]
final = lambda_function(list)
print(final)

# list comprehention for filter small strings

list = ["32","4","6","18","19"]
minlist = 1
list_comp = [item for item in list if len(item) <= minlist]
print(list_comp)




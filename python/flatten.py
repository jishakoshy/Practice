def flatten(array):
    result = []
    for row in array:
        for element in row:
            result.append(element)
    return result
array = [[23,4,5], [2,7,8]]
print(flatten(array))

# list = [3,5,7,3]
# x = list.pop()
# print(list)
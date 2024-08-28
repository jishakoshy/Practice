# find the sum of all numbers in a list or array//
arr = [1, 2, 3, {"a": 2}, {"ac": [1, 2, 3, {"b": 9}, [8]]}, [7, 7]]

sum = 0
num = str(arr)
for num in arr:
    sum += num
sum = int(sum)
print(sum)


# sum = 35 -> expected outcome

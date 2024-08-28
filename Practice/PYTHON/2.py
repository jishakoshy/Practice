
# i/p: lis = [(4,5), (1,8), (7,9),(5,3)]
# o/p: [(4,1),(4,3),(5,1),(5,5),(5,3),(8,4),
# (8,5),(8,1),(8,7),(8,5),(8,3),(7,5),(7,3),
# (7,1),(7,4),(3,1)]

lis = [(4, 5), (1, 8), (7, 9), (5, 3)]

flat_list = [item for sublist in lis for item in sublist]
                     # Convert the list into a tuple
# result = tuple(flat_list)
result = flat_list
print(result)

result = [4, 5, 1, 8, 7, 9, 5, 3]
filtered_combinations = []

# Use nested loops to generate pairs
for i in range(len(result)):
    for j in range(i + 1, len(result)):
        if result[i] > result[j]:
            filtered_combinations.append((result[i], result[j]))

print(filtered_combinations)



        







# def transform_list(input_list):
#     result = []
#     for a, b in input_list:
#         for i in range(1, b + 1):
#             result.append((b, i))
#         for i in range(1, a + 1):
#             if (i, b) not in result:
#                 result.append((i, b))
#     return result

# # Input list
# lis = [(4,5), (1,8), (7,9), (5,3)]

# # Get the transformed list
# output = transform_list(lis)

# # Print the result
# print(output)



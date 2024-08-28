student_info = {
    "Name" : "Alice",
    "age" :  27,
    "major" : "Computer Science",
    "graduation_year" : 2023
}
print(student_info)

# accessing dictionary items 
# 1. Using square brackets []
# 2. The get() method
# 3. Iterating through the dictionary using loops
# 4. Or specific methods like keys(), values(), and items()

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))

major = student_info.setdefault("major", "Computer Science")
print(student_info)

access = student_info["Name"]
print(access)

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana', 'Not found'))

access1 = student_info["age"]
print(access1)

access2 = student_info["major"]
print(access2)


student_info = {
    "Name": "Tressa",
    "age": 20,
    "major": ["Computer Science", 3, 5, (6, 7, 8, 9,{12,14,15,16,17}),{11,13}]
}

# Access the 9 from the major list
value_9 = student_info["major"][3][3]
print(value_9) 



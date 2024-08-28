student_info = {
    "Name" : "Tressa",
    "age" : 20,
    "major": "Computer Science"
}
# updation of value
student_info["age"] = 25
print(student_info)
# Updating Multiple Dictionary Values
student_info.update({'age':21,'Name':"jesus",'major':"engineering"})
print(student_info)

# Adding new key, value
student_info["graduation_year"] = 2021
print(student_info)

# deleting items
del student_info["major"]
print(student_info)

student_info.pop("age")
print(student_info)

student_info.popitem()
print(student_info)

del student_info["age"]
print(student_info)
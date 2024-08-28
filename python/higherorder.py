# higher order function in python is, a fuction which accept another function as argument 
#   or return a function

def add(a,b):
    return a+b

addition = add
                        #    
# print(add)
# print(addition)
# print(addition(10,20))


# def greet():
#     print("hi")

# def display(other_function):
#     print("this is display() function")
#     other_function()
# display(greet)

def greet_louder(name):
    print(f"Hi {name.upper()}")

def greet_softer(name):
    print(f"Hi {name.lower()}")

def hello(other_function,name):
    print("this is hello() function")
    other_function(name)
hello(greet_louder,"jisha")
hello(greet_softer,"JIsha")








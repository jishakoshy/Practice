# def sub(a,b):
#     print(a-b)

# def decor(sub):
#     def extra(a,b):
#         print(a+b)
#         print(a/b)
#         print(a*b)
#         # print(a-b)
#         return sub(a,b)
#     return extra

# final = decor(sub)
# final(100,50)



# def decor(sub):
#     def extra(a,b):
#         sub(a,b)
#         print(a+b)
#         print(a/b)
#         print(a*b)
#     return extra

# @decor
# def sub(a,b):
#     print(a-b)
# sub(20,10)



def decor(addition):
    def inner():
        result= addition()
        num3 = float(input("enter the third number"))
        result = result + num3
        return result
    return inner
    
@decor
def addition():
    num1 = float(input("enter the first number"))
    num2 = float(input("enter the second number"))
    result = num1 + num2
    return result

print(addition())

# def div(a,b):
#     print(a/b)

# def smart(func,a,b):
#         if a<b:
#             a,b= b,a
#         return func(a,b)
    
# div1 = smart(div,10,20)
# print(div1)

                          # or
# def div(a,b):
#     print(a/b)

# def outer(func):
#     def inside(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inside

# div = outer(div)
# div(10,20)


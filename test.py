def fact(n):
    if n<= 0:
        return None
    else:
        return n * fact(n-1)
n = int(input("enter number"))
print()

# 54321
# 4321
# 321
# 21
# 1

n = int(input("enter the num"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end= " ")
    print()



















# def keyword(**args):
#     x = a + b
#     print(x)

# keyword(a = 1, b =2) 


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Stack:
#         def __init__(self):
#             self.head = None

#         def push(self,data):
#             if self.head is None:
#                  self.head = Node(data)
#             else:
#                 newnode = Node(data)
#                 newnode.next = self.head
#                 self.head = newnode

#         def display(self):
#             if self.head is None:
#                  return None
#             current = self.head
#             print(current.data)
#             while current.next:               
#                 current = current.next
#                 print(current.data)

# s =  Stack()
# s.push(5)
# s.push(10)
# s.push(11)
# s.display()

                
            
            
# # def binary_search(arr, low, high, target):
# #     while low <= high:
# #         mid = low + (high - low) // 2
# #         if target == arr[mid]:
# #             return mid
# #         elif target < arr[mid]:
# #             high = mid - 1
# #         else:
# #             low = mid + 1
# #     return -1  # Return -1 if the target is not found

# # arr = [1, 2, 3, 4, 5, 6, 7]
# # target = 8
# # low = 0
# # high = len(arr) - 1
# # x = binary_search(arr, low, high, target)
# # print(x)






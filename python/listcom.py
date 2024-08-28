# list comprehension: filter dicts that don’t have a key

dict1 = { 1:"alice", 2:"aimy",3:"emil"}
x = dict1.keys()
print(x)

y = dict1.values()
print(y)

list1 = [1,2,2,2,3,3,4,5,5,5,5,5]
dict2 ={key:value for key,value in enumerate(list1) }
print(dict2)
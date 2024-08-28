# list comprehension that filter the specific key
list_dict = [{"name":"jisha","age":25,"city":"TVM"},
             {"name":"jolly","age":50},
             {"name":"sreya","age":40,"city":"WB"},
             {"city":"ernakulam"}]

list_com = [d for d in list_dict if "age" in  ]


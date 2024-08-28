# find duplicate with out using modifying the list

def duplicate(list):
    seen = set(list)
    for item in list:
        if item.list in seen:
            return item
        seen.add(item)
    return None

list = [3,4,6,7,5,4,3]
duplicate=duplicate(list)
print(duplicate)
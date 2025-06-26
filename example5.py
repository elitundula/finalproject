#Mutable Default Arguments
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2]
print(add_item(3))  # Output: [1, 2, 3]

print("that is it for part 1, now here is part 2")

def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [2]
print(add_item(3))  # Output: [3]

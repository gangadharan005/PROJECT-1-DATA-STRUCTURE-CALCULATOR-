# dict creation
def dict_create():
    d1 = int(input("enter the number: "))
    d2 = {}
    for i in range(0,d1):
        key = int(input())
        value = int(input())
        d2[key] = value
    return d2

# add method
def dict_add_method(dict1):
    key = int(input("enter the key (integer): "))
    value = int(input("enter the value (integer): "))
    dict1[key] = value
    return dict1

# replace method
def dict_replace_method(dict1):
    value = int(input("enter the value(integer): "))
    change_value = int(input("enter the changed value(integer): "))
    dict1[value] = change_value
    return dict1

# popitem method
def dict_popitem_method(dict1):
    dict1.popitem()
    return dict1

# update method
def dict_update_method(dict1,dict2):
    dict2.update(dict1)
    return dict2

# get key
def dict_get_key(dict1):
    return dict1.keys()

# get value
def dict_get_values(dict1):
    return dict1.values()

# length
def dict_length_method(dict1):
    return len(dict1)

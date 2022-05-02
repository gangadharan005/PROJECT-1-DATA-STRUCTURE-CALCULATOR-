# list create
def list_create_method():
    Li1 = int(input("please enter the single integer and create the list: "))
    Li2 = []
    for i in range(0, Li1):
        tem = int(input())
        Li2.append(tem)
    return Li2


# insert method
def insert_method(list1):
    Li3 = int(input("insert the position:"))
    Li4 = int(input("insert the new number:"))
    list1.insert(Li3, Li4)
    return list1


# Concatenation
def concatenation(list1, list2):
    list1 = int(input("Enter the adding element1: "))
    list2 = int(input("Enter the adding element2: "))
    list3 = list1 + list2
    return list3


# Extend
def extend_method(list1):
    list2 = int(input("enter the extend elements(single integer): "))
    list3 = int(input("enter the extend elements(single integer): "))
    list1.extend([list2,list3])
    return list1


# pop
def pop(list1):
    list2 = int(input("enter the pop elements(position):"))
    list1.pop(list2)
    return list1


# remove
def remove(list1):
    list2 = int(input("enter the remove element:"))
    list1.remove(list2)
    return list1


# count
def count_check(list1):
    counting_number = int(input("enter the count value : "))
    count2 = list1.count(counting_number)
    return count2


# sum
def sum_method(list1):
    return sum(list1)


# length
def length_method(list1):
    return len(list1)


#  Python program to print even numbers in a list
def even_check(list1):
    list2 = []
    for x in list1:
        if x % 2 == 0:
            list2.append(x)
    return list2


#  Python program to print odd numbers in a list
def odd_check(list1):
    list2 = []
    for x in list1:
        if x % 2 == 1:
            list2.append(x)
    return list2


# max
def max_method(list1):
    return max(list1)


# clear
def clear_method(list1):
    list1.clear()
    return list1


# copy
def copy_method(list1):
    list1.copy()
    return list1


# sort
def sort_method(list1):
    list1.sort()
    return list1


# min
def min_method(list1):
    return min(list1)


# duplicate removal:
def duplicate_removal(list1):
    value1 = int(input("enter the single integer: "))
    b = []
    for i in range(0, value1):
        temp = int(input())
        b.append(temp)
        c = set(b)
        d = tuple(c)
    return d

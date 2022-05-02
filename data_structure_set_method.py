# 1.set create
def set_create():
    s1 = int(input("Enter the integer:"))
    s2 = set()
    for i in range(0, s1):
        tem = int(input())
        s2.add(tem)
    return s2


# 2.update method
def set_update(set1, set2):
    set1.update(set2)
    return set(set1)


# 3.addition method
def set_add_method(set1):
    set2 = int(input("enter the adding element: "))
    set1.add(set2)
    return set1


# 4.remove method
def set_remove_method(set1):
    set2 = int(input("enter the remove element: "))
    set1.remove(set2)
    return set1


# 5.discard method
def set_discard_method(set1):
    set2 = int(input("Enter the discard number: "))
    set1.discard(set2)
    return set1


# 6.pop method
def set_pop_method(set1):
    set1.pop()
    return set1


# 7.clear method
def set_clear_method(set1):
    set1.clear()
    return set1


# 8.copy method
def set_copy_method(set1):
    set2 = set1.copy()
    return set2, id(set1), id(set2)


# 9.union method
def set_union_method(set1, set2):
    set3 = set1.union(set2)
    return set3


# 10.intersection method
def set_intersection_method(set1, set2):
    set3 = set1.intersection(set2)
    return set3

# 11.difference method
def set_difference(set1, set2):
    set3 = set1.difference(set2)
    return set3

# 12. symmetric difference method
def set_symmetric_difference(set1, set2):
    set3 = set1.symmetric_difference(set2)
    return set3


# 13. isdisjoint method
def set_isdisjoint_method(set1, set2, set3):
    set4 = set1.isdisjoint(set2)
    set5 = set1.isdisjoint(set3)
    return set4, set5


# 14. issuperset method
def set_issuperset_method(set1, set2, set3):
    set4 = set1.issuperset(set2)
    set5 = set1.issuperset(set3)
    return set4, set5


# 15.issubset method
def set_issubset_method(set1, set2):
    set3 = set2.issubset(set1)
    return set3

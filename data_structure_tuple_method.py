# tuple create
def tup_create_method():
    t1 = int(input("Enter the single integer: "))
    t2 = []
    for i in range(0, t1):
        tem = int(input())
        t2.append(tem)
    return tuple(t2)


# count
def count_method(tup1):
    t1 = int(input("enter the count value : "))
    t2 = tup1.count(t1)
    return t2


def index_method(tuple1):
    t1 = int(input("enter the index  value : "))
    t2 = tuple1.index(t1)
    return t2


# concatenate
def concatenate(tuple1, tuple2):
    tuple1 = int(input("enter the adding element1: "))
    tuple2 = int(input("enter the adding element2: "))
    tuple3 = tuple1 + tuple2
    return tuple3

# tuple conversion
def tuple_conversion():
    t1 = int(input("enter the integer:"))
    t2 = []
    for i in range(0,t1):
        temp = int(input())
        t2.append(temp)
        c = tuple(t2)
    return c,type(c)

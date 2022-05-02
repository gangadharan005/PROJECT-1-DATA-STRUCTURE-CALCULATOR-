import data_structure_list_method
import data_structure_tuple_method
import data_structure_set_method
import data_structure_dict_method

print("************** welcome to data structure calculator ********************")

while True:
    try:
        user_option = int(input("choose any one below the list:\n1.List\n2.tuple\n3.set\n4.Dictionary\nEnter the "
                                "number between 1 to 4: "))
    except ValueError:
        print("I don't understand")
        continue
    if user_option != '1' and user_option != '2' and user_option != '3' and user_option != '4':
        if user_option == 1:
            print("""***** please select below any ony operation *****:
                                        1.list create method
                                        2.insert method
                                        3.Concatenation
                                        4.Extend
                                        5.pop
                                        6.remove
                                        7.count
                                        8.sum
                                        9.length
                                        10.even check
                                        11.odd check
                                        12.max
                                        13.clear method
                                        14.copy method
                                        15.sort method
                                        16.min method
                                        17.duplicate removal""")
            while True:
                try:
                    user2 = int(input("select the number between 1 to 17: "))
                except ValueError:
                    print("I don't understand")
                    continue
                if (user2 != '1' and user2 != '2' and user2 != '3' and user2 != '4' and user2 != '5' and user2 != '6'
                        and user2 != '7' and user2 != '8' and user2 != '9' and user2 != '10' and user2 != '11'
                        and user2 != '12' and user2 != '13' and user2 != '14' and user2 != '15' and user2 != '16' and user2 != '17'):
                    if user2 == 1:
                        try:
                            print(data_structure_list_method.list_create_method())
                        except:
                            print("please enter the valid input")
                    if user2 == 2:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.insert_method(list1))
                        except:
                            print("please enter valid input")
                    if user2 == 3:
                        try:
                            list1 = data_structure_list_method
                            list2 = data_structure_list_method
                            print(data_structure_list_method.concatenation(list1, list2))
                        except:
                            print("invalid input")
                    if user2 == 4:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.extend_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 5:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.pop(list1))
                        except:
                            print("invalid input")
                    if user2 == 6:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.remove(list1))
                        except:
                            print("Invalid input")
                    if user2 == 7:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.count_check(list1))
                        except:
                            print("Invalid input")
                    if user2 == 8:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.sum_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 9:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.length_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 10:
                        try:

                            list1 = data_structure_list_method.list_create_method()
                            print("Even check")
                            print(data_structure_list_method.even_check(list1))
                        except:
                            print("Invalid input")
                    if user2 == 11:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print("ODD CHECK")
                            print(data_structure_list_method.odd_check(list1))
                        except:
                            print("Invalid input")
                    if user2 == 12:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print("Maximum number is: ")
                            print(data_structure_list_method.max_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 13:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.clear_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 14:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print(data_structure_list_method.copy_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 15:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print("sorting order")
                            print(data_structure_list_method.sort_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 16:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print("Minimum value is:")
                            print(data_structure_list_method.min_method(list1))
                        except:
                            print("Invalid input")
                    if user2 == 17:
                        try:
                            list1 = data_structure_list_method.list_create_method()
                            print("Duplicate removal")
                            print(data_structure_list_method.duplicate_removal(list1))
                        except:
                            print("Invalid input")
                    user_list_continue = input("Do you want calculate again (yes/no)?: ").lower()
                    if user_list_continue in ['yes', 'y']:
                        continue
                    else:
                        break
            back_to_main_program = input("Do you want go to main program (yes/no)?: ").lower()
            if back_to_main_program in ['yes', 'y']:
                pass
            else:
                print("******EXIT******")
                break

        elif user_option == 2:
            print("""***** Welcome to Tuple method *****
                      1.Tuple create method 
                      2.Tuple count method
                      3.Tuple index method
                      4.Tuple concatenation method
                      5.list to tuple conversion method""")
            while True:
                try:
                    user3 = int(input("Enter the number between 1 to 5:"))
                except ValueError:
                    print("I don't understand")
                    continue

                if user3 != '1' and user3 != '2' and user3 != '3' and user3 != '4' and user3 != '5':
                    if user3 == 1:
                        try:
                            print(data_structure_tuple_method.tup_create_method())
                        except:
                            print("Invalid input")
                    if user3 == 2:
                        try:
                            tup1 = data_structure_tuple_method.tup_create_method()
                            print(data_structure_tuple_method.count_method(tup1))
                        except:
                            print("invalid input")
                    if user3 == 3:
                        try:
                            tup1 = data_structure_tuple_method.tup_create_method()
                            print(data_structure_tuple_method.index_method(tup1))
                        except:
                            print("invalid input")
                    if user3 == 4:
                        try:
                            tuple1 = data_structure_tuple_method
                            tuple2 = data_structure_tuple_method
                            print(data_structure_tuple_method.concatenate(tuple1, tuple2))
                        except:
                            print("invalid input")
                    if user3 == 5:
                        try:
                            print(data_structure_tuple_method.tuple_conversion())
                        except:
                            print("Invalid input")
                    user_tuple_continue = input("Do you want calculate again (yes/no)?: ").lower()
                    if user_tuple_continue in ['yes', 'y']:
                        continue
                    else:
                        break
            back_to_main_program_tuple = input("Do you want go to main program (yes/no)?: ").lower()
            if back_to_main_program_tuple in ['yes', 'y']:
                pass
            else:
                print("******EXIT******")
                break
        elif user_option == 3:
            print("""***** Welcome to set method *****
                               1.set create
                               2.update method
                               3.addition method
                               4.remove method
                               5.discard method
                               6.pop method
                               7.clear method
                               8.copy method
                               9.union method
                               10.intersection method                 
                               11.difference method                  
                               12.symmetric difference method                  
                               13.isdisjoint method
                               14.issuperset method
                               15.issubset method""")
            while True:
                try:
                    user4 = int(input("select the number between 1 to 15: "))
                except ValueError:
                    print("I don't understand")
                    continue
                if (user4 != '1' and user4 != '2' and user4 != '3' and user4 != '4' and user4 != '5' and user4 != '6'
                        and user4 != '7' and user4 != '8' and user4 != '9' and user4 != '10' and user4 != '11'
                        and user4 != '12' and user4 != '13' and user4 != '14' and user4 != '15'):
                    if user4 == 1:
                        try:
                            print(data_structure_set_method.set_create())
                        except:
                            print("invalid input")
                    if user4 == 2:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            print("update value is:")
                            print(data_structure_set_method.set_update(set1, set2))
                        except:
                            print("enter the valid operation")
                    if user4 == 3:
                        try:
                            set1 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_add_method(set1))
                        except:
                            print("Invalid input")
                    if user4 == 4:
                        try:
                            set1 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_remove_method(set1))
                        except:
                            print("invalid input")
                    if user4 == 5:
                        try:
                            set1 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_discard_method(set1))
                        except:
                            print("Invalid input")
                    if user4 == 6:
                        try:
                            set1 = data_structure_set_method.set_create()
                            print("Pop method")
                            print(data_structure_set_method.set_pop_method(set1))
                        except:
                            print("Invalid input")
                    if user4 == 7:
                        try:
                            set1 = data_structure_set_method.set_create()
                            print("clear method")
                            print(data_structure_set_method.set_clear_method(set1))
                        except:
                            print("Invalid input")
                    if user4 == 8:
                        try:
                            set1 = data_structure_set_method.set_create()
                            print("copy method")
                            print(data_structure_set_method.set_copy_method(set1))
                        except:
                            print("Invalid input")
                    if user4 == 9:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            print("Union method")
                            print(data_structure_set_method.set_union_method(set1, set2))
                        except:
                            print("invalid input")
                    if user4 == 10:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            print("Intersection method")
                            print(data_structure_set_method.set_intersection_method(set1, set2))
                        except:
                            print("invalid input")
                    if user4 == 11:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            print("difference method")
                            print(data_structure_set_method.set_difference(set1, set2))
                        except:
                            print("invalid input")
                    if user4 == 12:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_symmetric_difference(set1, set2))
                        except:
                            print("invalid input")
                    if user4 == 13:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            set3 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_isdisjoint_method(set1, set2, set3))
                        except:
                            print("invalid input")
                    if user4 == 14:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            set3 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_issuperset_method(set1, set2, set3))
                        except:
                            print("invalid input")
                    if user4 == 15:
                        try:
                            set1 = data_structure_set_method.set_create()
                            set2 = data_structure_set_method.set_create()
                            print(data_structure_set_method.set_issubset_method(set1, set2))
                        except:
                            print("invalid input")
                    user_set_continue = input("Do you want calculate again (yes/no)?: ").lower()
                    if user_set_continue in ['yes', 'y']:
                        continue
                    else:
                        break
            back_to_main_program_set = input("Do you want go to main program (yes/no)?: ").lower()
            if back_to_main_program_set in ['yes', 'y']:
                pass
            else:
                print("******EXIT******")
                break
        elif user_option == 4:
            print(""" Welcome to dictionary method:
                              1.dict creation
                              2.add method
                              3.replace method
                              4.popitem method
                              5.update method
                              6.get key
                              7.get value
                              8.length""")
            while True:
                try:
                    user5 = int(input("select the number between 1 to 15: "))
                except ValueError:
                    print("I don't understand")
                    continue
                if (user5 != '1' and user5 != '2' and user5 != '3' and user5 != '4' and user5 != '5' and user5 != '6'
                        and user5 != '7' and user5 != '8'):
                    if user5 == 1:
                        try:
                            print(data_structure_dict_method.dict_create())
                        except:
                            print("invalid input")
                    if user5 == 2:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            print("The added value is:")
                            print(data_structure_dict_method.dict_add_method(d1))
                        except:
                            print("invalid input")
                    if user5 == 3:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            print("Replace method")
                            print(data_structure_dict_method.dict_replace_method(d1))
                        except:
                            print("invalid input")
                    if user5 == 4:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            print("Popitem method")
                            print(data_structure_dict_method.dict_popitem_method(d1))
                        except:
                            print("invalid input")
                    if user5 == 5:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            d2 = data_structure_dict_method.dict_create()
                            print(data_structure_dict_method.dict_update_method(d1, d2))
                        except:
                            print("Invalid input")
                    if user5 == 6:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            print("keys:")
                            print(data_structure_dict_method.dict_get_key(d1))
                        except:
                            print("invalid input")
                    if user5 == 7:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            print("values:")
                            print(data_structure_dict_method.dict_get_values(d1))
                        except:
                            print("invalid input")
                    if user5 == 8:
                        try:
                            d1 = data_structure_dict_method.dict_create()
                            print("Length:")
                            print(data_structure_dict_method.dict_length_method(d1))
                        except:
                            print("Invalid input")
                    user_dict_continue = input("Do you want calculate again (yes/no)?: ").lower()
                    if user_dict_continue in ['yes', 'y']:
                        continue
                    else:
                        break
            back_to_main_program_dict = input("Do you want go to main program (yes/no)?: ").lower()
            if back_to_main_program_dict in ['yes', 'y']:
                pass
            else:
                print("***************EXIT*****************")
                break

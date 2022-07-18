#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            new_list.insert(i, (my_list_1[i] / my_list_2[i]))
        except ZeroDivisionError:
            print("division by 0")
            new_list.insert(i, 0)
            continue
        except (ValueError, TypeError):
            print("wrong type")
            new_list.insert(i, 0)
            continue
        except IndexError:
            print("out of range")
            new_list.insert(i, 0)
        finally:
            pass
    return new_list

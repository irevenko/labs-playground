from tkinter import messagebox


def unique(set_list):
    same_numbers = [] 
    for item in set_list:
        if item not in same_numbers:
            same_numbers.append(item)
    return same_numbers


def in_order(final_set):
    temp_set = []
    total_sets = []
    result = ""
    for x in range(0, len(final_set)):
        if len(temp_set) == 0:
            temp_set.append(final_set[x])
            continue
        if temp_set[-1] + 1 == final_set[x]:
            temp_set.append(final_set[x])
            if len(final_set) - 1 == x:
                total_sets.append(temp_set)
                continue
        else:
            total_sets.append(temp_set)
            temp_set = [final_set[x]]
    for x in total_sets:
        if len(x) > 1:
            result += f"{x[0]}-{x[-1]} "
    messagebox.showinfo("Union | ∪ ","{" + result[:-1] + "}")

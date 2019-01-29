lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_copy = lst[3:7]
print(lst_copy)
lst_copy.reverse()
print(lst_copy)
lst[3:7] = lst_copy
print(lst)

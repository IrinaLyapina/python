my_list_1 = [2, 2, 5, 12, 8, 2, 12]
new_list = []
i = 0
while i < len(my_list_1):
    if my_list_1.count(my_list_1[i]) == 1:
        new_list.append(my_list_1[i])
    i = i + 1

print(new_list)



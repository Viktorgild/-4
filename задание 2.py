my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
dic = my_list[1:]
my_new_list = [el for num, el in enumerate(dic) if dic[num - 1] < dic[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

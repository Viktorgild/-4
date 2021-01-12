my_list = [1, 1, 2, 2, 3, 4, 5, 5, 6, 65, 46, 4, 65]
for x in my_list:
    if my_list.count(x) < 2:
        print(x)
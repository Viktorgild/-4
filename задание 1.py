def my_func(arg_1, arg_2, arg_3):
    res = arg_1 * arg_2 + arg_3
    return res - (res * .13)


x = int(input("Введите выработку в часах :"))
y = int(input("Введите вашу ставку :"))
s = int(input("Введите вашу премию :"))

print(my_func(x, y, s))
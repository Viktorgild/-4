def my_func():
    for el in (10, n):
        yield el

fanc = my_func()
print(fanc)

n = int(input("Введите число:"))
for el in fanc:
    print(el)

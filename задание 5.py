# print(list(range(100, 1000)))
from functools import reduce


def my_func(x, xl):
    return x * xl


for x in range(100, 1001):
    if x % 2 == 0:
        print(f"Четные числа  {x}")

print(f"Результат вычисления всех элементов {reduce(my_func, [x for x in range(100, 1001) if x % 2 == 0])}")
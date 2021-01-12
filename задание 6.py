from itertools import count

for x in count(3):
    if x > 10:
        break
    print(x)

s = int(input("какое максимальное число вы хотите высести? :"))
for x in count(0):
    if x >= s:
        break
    print(x)

s = int(input("Введите колличество повторений :"))
from itertools import cycle

c = 0
for el in cycle('Hello, World'):
    if c >= s:
        break
    print(el)
    c += 1

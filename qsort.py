from random import randint
import timeit

# Быстрая сортировка

def qsort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = []
        right = []
        middle = []
        for i in arr:
            if i > pivot:
                right.append(i)
            elif i < pivot:
                left.append(i)
            else:
                middle.append(i)
        return qsort(left) + middle + qsort(right)

# Сортировка вставками

def insertion(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        i2 = i - 1
        while i2 >= 0 and arr[i2] > item:
            arr[i2 + 1] = arr[i2]
            i2 -= 1
            arr[i2 + 1] = item

    return arr


thousand = []                   # список из 1000 чисел
for i in range(1000):
    thousand.append(randint(0, 10000))

hundred = []                    # список из 100 чисел
for i in range(100):
    hundred.append(randint(0, 1000))

ten = []
for i in range(10):
    ten.append(randint(0, 100))



def qsearch():
    arr =  thousand             # сюда подставляем все списки
    qsort(arr)

def isearch():
    arr =  thousand             # сюда подставляем все списки
    insertion(arr)

print(timeit.timeit(stmt = "qsearch()", globals=globals(), number = 1000))
print(timeit.timeit(stmt = "isearch()", globals=globals(), number = 1000))

# Сравнение времени выполнения на разных длинах:
# qsort, длина 10 элементов - 0,003
# insertion, длина 10 элементов - 0,0005
# qsort, длина 100 элементов - 0,044
# insertion, длина 100 элементов - 0,0047
# qsort, длина 1000 элементов - 0,63
# insertion, длина 1000 элементов - 0,069


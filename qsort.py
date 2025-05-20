from random import randint

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

thousand = []                   # список из 1000 чисел
for i in range(1000):
    thousand.append(randint(0, 10000))

hundred = []                    # список из 100 чисел
for i in range(100):
    hundred.append(randint(0, 1000))

ten = []
for i in range(10):
    ten.append(randint(0, 100))
arr = thousand
print(arr)
print(qsort(arr))
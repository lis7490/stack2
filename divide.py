from random import randint
def divide(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        divide(left_half)
        divide(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len (right_half):
            if left_half[i] < right_half [j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr[-1]

arr = []
for i in range(10):
    arr.append(randint(0, 100))
print(arr)
print(divide(arr))
def insertion(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        i2 = i - 1
        while i2 >= 0 and arr[i2] > item:
            arr[i2 + 1] = arr[i2]
            i2 -= 1
            arr[i2 + 1] = item

    return arr
arr = [54, 43, 3, 11, 0]
print(insertion(arr))



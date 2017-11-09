def insertionsort(arr):
    i = 0
    while( i < len(arr) ):
        temp  = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j ]
            j -= 1
        arr[j + 1] = temp
        i += 1
    return arr
arr = [12, 11, 13, 5, 6]
print(insertionsort(arr))
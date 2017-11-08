def selectionsort(arr):
    i=0
    while i < len(arr):
        j = i+1
        while j < len(arr):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
            j += 1
        i += 1
    return arr


print selectionsort([64, 25, 12, 22, 11])
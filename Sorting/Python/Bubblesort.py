def bubble(arr):
    i=0
    count = 0
    while(i < len(arr)):
        j = 0 
        flag = True
        while( j < len(arr) - i - 1):
            count += 1
            if arr[j] > arr[j +1 ]:
                flag = False
                
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        if flag:
            break
        i += 1
    
    return arr
print(bubble([5 ,1 ,4, 2, 8]))
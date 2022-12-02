

def mergeSort(arr):
   
    if len(arr)>1:
        half = len(arr)//2
        a = arr[:half]
        b = arr[half:]
        mergeSort(a)
        mergeSort(b)
        
        i = j = k = 0

        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
            
 
    
        while i < len(a):
            arr[k] = a[i]
            i += 1
            k += 1
 
        while j < len(b):
            arr[k] = b[j]
            j += 1
            k += 1
        
        return arr


arr=[2,8,4,9,1,3,7,5]

print(mergeSort(arr))

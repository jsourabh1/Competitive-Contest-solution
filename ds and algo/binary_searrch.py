def binary_search(arr,key):



    if len(arr)==0:return 

    mid=len(arr)//2

    if arr[mid]==key:
        return mid

    if arr[mid]<key:
        return binary_search(arr[mid+1:],key)
    else:

        return binary_search(arr[:mid],key)

    return 

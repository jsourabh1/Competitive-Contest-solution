


def solve(arr):
    # sort the array in asending order
    n=len(arr)

    for i in range(1,n):
        key =arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)

    #sort array in desescnding order


    for i in range(1,n):
        key=arr[i]
        j=i-1
        
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)
    
    


arr=[4,3,2,1]
solve(arr)
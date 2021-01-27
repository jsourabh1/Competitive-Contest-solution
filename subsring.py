import re
for _ in range(int(input())):

    n,m=map(int,input().split())
    arr=str(input())
    for i in range(m):
        l,r=map(int,input().split())
        if l==r:
            print("No")
        else:
            
            string=arr[l-1:r]  #010
            #print(string)
            fin=string[-1] #0
            #print(fin)
            index=arr.find(string[:len(string)-1])  #1
            #print(index)
            another1=arr[:index]
            index+=(len(string)-1)  #3
            #print("up",index)
            another=arr[index+1:]
            #print(another)
            if another.find(fin)==-1 and another1.find(fin)==-1:
                print("No")
            else:
                print("Yes")
            
            '''
            string=arr[l-1:r]
            print(string)
            for i in range(len(string)):

                if i==(len(string)-1):
                    index = arr[prev + 1:].rfind(string[i])
                    if index-prev<=1:
                        print("No")
                    else:
                        print("Yes")


                print(arr[prev+1:])
                index=arr[prev+1:].find(string[i])
                prev=index
                print(prev,index)


                '''

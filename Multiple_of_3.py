def solve(n,d1,d2):
    number = str(d1) + str(d2)
    res = n - 3
    string = ""
    for i in range(5):
        j = int((math.pow(2, i) * int(d1 + d2)) % 10)
       
        if i > 0:
            string += str(j)
        number += str(j)

    #print(number,string)
        
        
    if n>7:

        sum2 = int(number[0]) + int(number[1]) + int(number[2]) 
                
        #print(sum2)
        if res % 4 == 0:

            sum2 += 20 * (res // 4)
        else:
            index = res % 4
            #print(index,20 * (res // 4))
            sum2 += 20 * (res // 4)
            #print(sum2)
            stri = string[:index]
            for i in stri:
                sum2 += int(i)
           # print(sum2)
    else:
        sum2=0
        for i in number[:n]:
            sum2+=int(i)

    #print(sum2)
    if sum2 % 3 == 0:
        print("YES")
    else:
        print("NO")
    
    
    return



import math

for _ in range(int(input())):

    n, d1, d2 = map(int, input().split())
    
    solve(n,d1,d2)
    

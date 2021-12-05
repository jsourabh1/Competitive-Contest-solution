from collections import defaultdict

#brute force in the exponential time 



def solve(number, ans, index, arr, dict_1):
    # print(number)

    if len(number) == 3:
        # print(number,number[0])
        if number[0] != '0':
            ans.append(int(number))

    if index > len(arr):
        return
    # print(index)
    for i in range(len(arr)):
        # print(i,arr[i])

        if dict_1[arr[i]] > 0:
            dict_1[arr[i]] -= 1
            # print(str(arr[i])+number)

            solve(str(arr[i]) + number, ans, i + 1, arr, dict_1)

            dict_1[arr[i]] += 1

    return


class Solution:
    def findEvenNumbers(self, digit: List[int]) -> List[int]:

        even = []
        dict_1 = defaultdict(lambda: 0)

        for i in digit:

            if i % 2 == 0:
                even.append(i)

            dict_1[i] += 1

        ans = []

        for i in even:
            dict_1[i] -= 1

            solve(str(i), ans, 0, digit, dict_1)

            dict_1[i] += 1
        return sorted(list(set((ans))))


#upper approach from the brute 
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        
        ans=set()
        for x,y,z in permutations(digits,3):
            
            if x!=0 and z%2==0:
                
                ans.add(x*100+y*10+z)
                
        return sorted(ans)
        

#optimizes approach 


class Solution(object):
    def findEvenNumbers(self, digits):
       
        n = len(digits)
        fre = [0]*10
        for i in range(n):
            fre[digits[i]] += 1
        ans = []
        for i in range(1,10):
            if fre[i]==0: continue 
            fre[i] -= 1
            for j in range(10):
                if fre[j]==0: continue 
                fre[j] -= 1
                for k in range(0,10,2):
                    if fre[k]==0: continue 
                    fre[k] -= 1
                    ans.append(i*100+j*10+k)
                    fre[k] += 1            
                fre[j] += 1        
            fre[i] += 1   
        return ans


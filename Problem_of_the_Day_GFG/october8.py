#User function Template for python3
from collections import defaultdict

dict_1=defaultdict(lambda:-1)
class Solution:
	def TotalAnimal(self, n):
		# Code here
		global dict_1
		
		def fib(n):
		    
		
    		if n==0 :return 0
            if n==2 or  n==1: return 1
            
            if n in dict_1:
                return dict_1[n]
                
            if n%2!=0:
                k=(n+1)//2;
                dict_1[n]=(fib(k)*fib(k)+fib(k-1)*fib(k-1))%1000000007
            
            else:
                k=n//2;
                dict_1[n]=(fib(k)*((fib(k-1)<<1)+fib(k)))%1000000007
            return dict_1[n]
            
        return fib(n+1)



# Idea is to use Fibonacci series where n= n+1.

# But here n is very large so we will use formula to recur with memoization

# F(2n) = F(n)[2*F(n+1) – F(n)]
# F(2n + 1) = F(n)2 + F(n+1)2
		
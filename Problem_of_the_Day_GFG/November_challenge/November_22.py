#User function Template for python3
class Solution:
  def minJumps(self, arr, n):
      
     if len(arr)==1:
          return 0
      
     last=n-1
     
     for i in range(n-2,-1,-1):
         
         if i+arr[i]>=last:
             last=i
             
     if last!=0:
         return -1
         
     steps=1
     currjump=arr[0]
     maxjump=arr[0]
     
     for i in range(n-1):
         
         maxjump=max(maxjump,i+arr[i])
         
         if currjump==i:
             steps+=1
             currjump=maxjump
             
     return steps
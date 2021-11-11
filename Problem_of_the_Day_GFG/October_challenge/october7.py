#User function Template for python3

class Solution:
    def maxFrequency(self, S):
        # code here
        
        
        left=0
        right=len(S)-1
        left_s=""
        right_s=""
        while left<len(S) and right>=0:
            
            left_s+=S[left]
            right_s=S[right]+right_s
            
            if left_s==right_s:
                break
            left+=1
            right-=1
            
        return S.count(left_s)
            
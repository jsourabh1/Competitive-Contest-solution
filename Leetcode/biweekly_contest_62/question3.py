# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

from collections import defaultdict
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        dict_1=defaultdict(lambda:0)
        
        # for changing the all true to false
        
        left=right=count=0
        
        ans=-float("inf")
        while right<len(answerKey):
            
            if answerKey[right]=="F":
                
                ans=max(ans,right-left+1)
                
            else:
                
                count+=1
                if count>k:
                    
                    while count>k and left<=right:
                        
                        if answerKey[left]=="T":
                            count-=1
                        left+=1
                            
                    
                ans=max(ans,right-left+1)
                
            right+=1
            
        print(ans)
        
        # for changing the false to true
        
        left=right=count=0
        
        
        while right<len(answerKey):
            
            if answerKey[right]=="T":
                
                ans=max(ans,right-left+1)
                
            else:
                
                count+=1
                if count>k:
                    
                    while count>k and left<=right:
                        
                        if answerKey[left]=="F":
                            count-=1
                        left+=1
                            
                    
                ans=max(ans,right-left+1)
            # print(ans,left,right)
                
            right+=1
            
        return ans
            
        
                        
        
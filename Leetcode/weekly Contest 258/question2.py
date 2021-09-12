
        #question for practisehttps://leetcode.com/contest/weekly-contest-258/problems/number-of-pairs-of-interchangeable-rectangles/
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        
        dict_1=defaultdict(lambda:0)
        
        count=0
        
        for width,height in rectangles:
            
            
            
            if width/height in dict_1:
                
                count+=dict_1[width/height]
                dict_1[width/height]+=1
                
            else:
                dict_1[width/height]=1
                
            # print(dict_1)
                
        return count
            
        
        
        
        
        
        
        
class Solution:
    def reverseWords(self, s: str) -> str:
        
        listt=list(map(str,s.split()))
        
        return " ".join(listt[::-1])

		#question for practisehttps://leetcode.com/contest/weekly-contest-258/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch not in word:
            return word
        
        index1=word.index(ch)
        
        ans=word[:index1+1][::-1]+word[index1+1:]
        return ans
        
        
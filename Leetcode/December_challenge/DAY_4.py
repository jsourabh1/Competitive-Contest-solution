# TLE code 


class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.arr=words
        self.length=len(min(words,key=len))
        # print(self.length)
        self.string=""

        

    def query(self, letter: str) -> bool:
        
        self.string+=letter
        
        for i in range(-self.length+len(self.string)+1):
            # print()
            # print( self.string[i:] )
            
            if self.string[i:] in self.arr:
                return True
            
        return False
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)






# ACCEPTED CODE


from collections import defaultdict
class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.s=""
        self.dic=defaultdict(set)
        
        for i in words:
            
            self.dic[i[-1]].add(i)
        

    def query(self, letter: str) -> bool:
        
        self.s+=letter
        
        return any(self.s.endswith(w) for w in self.dic[letter])
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
from random import *
from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_1=defaultdict(None)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict_1:
            self.dict_1[val]=True
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        index = self.dict_1.get(val, None)
        if index!=None:
            del self.dict_1[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(list(self.dict_1.keys()))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()from random import *
from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_1=defaultdict(None)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict_1:
            self.dict_1[val]=True
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        index = self.dict_1.get(val, None)
        if index!=None:
            del self.dict_1[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(list(self.dict_1.keys()))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
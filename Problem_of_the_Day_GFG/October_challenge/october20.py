class MyQueue:
    def __init__(self):
        
        self.arr=[]
    #Function to push an element x in a queue.
    def push(self, x):
         
        self.arr.append(x)
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        
        if not self.arr:
            return -1
            
        return self.arr.pop(0)
         
         # add code here
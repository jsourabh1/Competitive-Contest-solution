class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		
		visited=set()
		self.graph=adj
		for i in range(V):
		    
		    if i not in visited:
		        
		        if self.helper(visited,i,-1):
		            return True
		            
		return False
		 
    def helper(self,visited,node,parent):
        
        visited.add(node)
        
        
        for  i in self.graph[node]:
            
            if i not in visited:
                
                if self.helper(visited,i,node):
                    return True
                    
            elif parent!=i:
                return True
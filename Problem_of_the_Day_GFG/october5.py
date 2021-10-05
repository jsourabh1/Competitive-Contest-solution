#User function Template for python3
from collections import defaultdict
class Solution:
    def solve(self, n, p ,a, b, d): 
        #code here
        
        
        def dfs(node,visited,ans,graph):
            
            visited.add(node)
            ans.append(node)
            for i in graph[node]:
                
                if i not in visited:
                    
                    return dfs(i,visited,ans,graph)
            
            return ans
            
        graph1=defaultdict(list) #incoming edge
        graph2=defaultdict(list)  #outgoing edge
        
        for i in range(p):
            graph1[b[i]].append(a[i])
            graph1[b[i]].append(d[i])
            graph2[a[i]].append(b[i])
        ans=[]
        for i in a:
            
            if not graph1[i]:
                temp=[]
                visited=set()
                ans.append(dfs(i,visited,temp,graph2))
        anss=[]
        ans.sort()
        for i in ans:
            dia=float("inf")
            
            for j in i[1:]:
                dia=min(dia,graph1[j][1])
            anss.append([i[0],i[-1],dia])
        return anss
            
            
            
        
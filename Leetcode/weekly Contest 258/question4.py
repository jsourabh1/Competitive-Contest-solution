# question link: https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        
        n=len(parents)
        
        g=[[] for i in range(n)]
        
        for i,res in enumerate(parents):
            
            if res!=-1:
                g[res].append(i)
                
        res=[1]*(n)
        
        if 1 not in nums:
            return res
        # print(g)
        seen = [False] * (n+1)
        def scan(p,prev):
            
            if nums[p]<=n: seen[nums[p]]=True
            # print(prev,p)
            for i in g[p]:
                if i!=prev:
                    scan(i,-1)
                    
                    
        prev,p=-1,nums.index(1)
        
        curr=0
        
        while p!=-1:
            
            scan(p,prev)
            # print(prev,p)
            
            while curr+1<=n and seen[curr+1]:
                curr+=1
            # print(curr,seen,res)
            res[p]=curr+1
            
            prev,p=p,parents[p]
            # print()
            
        return res
        
                
        
        
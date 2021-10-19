class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)==1:
            return 0
        
        maxx=-float("inf")
        minn=float("inf")
        arr1=[]
        maxprofit=0
        for i in prices:
            
            minn=min(minn,i)
            
            maxprofit=max(maxprofit,i-minn)
            
            arr1.append(maxprofit)
            
        ans=0
        m=0
        # print(arr1)
        for i in range(len(prices)-1,-1,-1):
            
            maxx=max(maxx,prices[i])
            m=max(m,maxx-prices[i])
            ans=max(ans,m+arr1[i])
            # print(m)
        return ans
            
            
        
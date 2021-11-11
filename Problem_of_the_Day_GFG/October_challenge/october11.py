class Solution:
	def overlappedInterval(self, intervals):
		#Code here
		
		ans=[]
		
		intervals=sorted(intervals)
# 		print(intervals)
		
		first=intervals[0][0]
		second=intervals[0][1]
		
		for i in intervals[1:]:
		    
		    if second>=i[0]:
		        if second>=i[1]:
		            continue
		        else:
		            second=i[1]
		    else:
		        ans.append([first,second])
		        first=i[0]
		        second=i[1]
		ans.append([first,second])
		return ans
		
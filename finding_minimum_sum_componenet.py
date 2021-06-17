def addedge(u,v):

	global adj

	adj[u].append(v)

def dfs(node,minn,visit):
	global adj,arr

	minn=min(minn,arr[node-1])

	visit.add(node)

	for i in adj[node]:

		if i not in visit:

			dfs(i,minn,visit)

def Helper():
	global arr
	summ=0
	visit=set()
	minn=0
	for i in range(1,len(arr)+1):

		if i not in visit:
			minn=arr[i-1]

			dfs(i,minn,visit)
			# print(minn)
			summ+=minn

	print(summ)


arr= [2, 5, 3, 4, 8]

from collections import defaultdict
adj=defaultdict(list)
addedge(1, 4);
addedge(4, 5);

Helper()
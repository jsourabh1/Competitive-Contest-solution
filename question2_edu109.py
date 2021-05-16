#quesiton link:-https://codeforces.com/contest/1525/problem/B
'''

You are given a permutation a consisting of n numbers 1, 2, ..., n (a permutation is an array in which each element from 1 to n occurs exactly once).

You can perform the following operation: choose some subarray (contiguous subsegment) of a and rearrange the elements in it in any way you want. But this operation cannot be applied to the whole array.

For example, if a=[2,1,4,5,3] and we want to apply the operation to the subarray a[2,4] (the subarray containing all elements from the 2-nd to the 4-th), then after the operation, the array can become a=[2,5,1,4,3] or, for example, a=[2,1,5,4,3].

Your task is to calculate the minimum number of operations described above to sort the permutation a in ascending order.



'''

#solution :-

for _ in range(int(input())):
	n=int(input())

	arr=list(map(int,input().split()))

	sort_arr=sorted(arr)

	if arr==sort_arr:
		print(0)
		#return 
	elif arr[0]==sort_arr[0] or arr[-1]==sort_arr[-1]:
		print(1)
		#return 
	elif arr[0]==sort_arr[-1] and arr[-1]==sort_arr[0]:
		print(3)
		#return
	else:
		print(2)
	
 
 
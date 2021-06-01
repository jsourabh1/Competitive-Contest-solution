def merge(left,right,arr):
	n1=len(left)
	n2=len(right)
	i=j=k=0
	print(left,right)
	while i<n1 and j<n2:

		if left[i]<=right[j]:
			arr[k]=left[i]
			i+=1
			k+=1
		else:
			arr[k]=right[j]
			j+=1
			k+=1

	while i<n1:
		arr[k]=left[i]
		k+=1
		i+=1
	while j<n2:
		arr[k]=right[j]
		j+=1
		k+=1
	return



def merge_sort(arr):
	n=len(arr)
	if n>=2:
		mid=n//2
		left=arr[:mid]
		right=arr[mid:]
		print(left,right)
		merge_sort(left)
		merge_sort(right)
		merge(left,right,arr)
   


arr=[4,42,3]
merge_sort(arr)
print(arr)

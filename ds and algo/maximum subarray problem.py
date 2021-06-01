# this is the brute force of the maximum subarray problem with time compexity is n^2

'''
arr=[-1, -2, 3, 5, 4, -1, -10, -15, -20]


maxx=-999999999999999999999999

for i in range(len(arr)):
    sum=0
    for j in range(i,len(arr)):

        sum+=arr[j]
        if sum>maxx:
            maxx=sum

print(maxx)




with  time complexity is nlogn

			max_left=i

	right_sum=-99999999
def cross_subarray(arr,low,mid,high):
	#print(low,mid,high)

	left_sum=-9999999999999999999
	summ=max_left=0

	for i in range(mid,low-1,-1):
		summ+=arr[i]
		if summ>left_sum:
			left_sum=summ999999999
	summ=max_right=0

	for j in range(mid+1,high+1):
		summ+=arr[j]

		if summ>right_sum:
			right_sum=summ
			max_right=i
	#print(right_sum,left_sum)
	return max_left,max_right,left_sum+right_sum


def max_subarray(arr,low,high):
	#print(arr[low:high+1],low,high)

	if low==high:
		return low,high,arr[low]

	else:
		mid=(low+high)//2

		left_low,left_high,left_sum=max_subarray(arr,low,mid)
		right_low,right_high,right_sum=max_subarray(arr,mid+1,high)
		cross_low,cross_high,cross_sum=cross_subarray(arr,low,mid,high)
		#print(arr[low:high+1],left_sum,cross_sum,right_sum)
		#print()

		if left_sum>=right_sum and left_sum>=cross_sum:

			return left_low,left_high,left_sum
		elif right_sum>=left_sum and right_sum>=cross_sum:

			return right_low,right_high,right_sum

		else:
			return cross_low,cross_high,cross_sum

	#print()


arr=[-1,-2,3,5,4,-1,-10,-15,-20]
print(max_subarray(arr,0,len(arr)-1))

# when we allow thee emppty array can be our answer


def cross(arr,low,mid,high):

    left_sum=-99999999999999999999999999
    sum=0
    for i in range(mid,low-1,-1):
        sum+=arr[i]
        if sum>left_sum:
            left_sum=sum
    right_sum=-99999999999999999999999999
    sum=0
    for i in range(mid+1,high+1):
        sum+=arr[i]
        if sum>right_sum:
            right_sum=sum

    return left_sum+right_sum


def max_subarray(arr,low,high):

    if low==high:
        return arr[low]

    else:

        mid=(low+high)//2

        left_sum=max_subarray(arr,low,mid)
        right_sum=max_subarray(arr,mid+1,high)
        cross_sum=cross(arr,low,mid,high)

        return max(cross_sum,right_sum,left_sum,0)

arr=[-1,-2,-3,-4,-4]
flag=0
for i in arr:
    if i>0:
        flag=1
if flag==1:

    print(max_subarray(arr,0,len(arr)-1))
else:
    print("all are negative ",0)

'''

# the linear time implementation of the maximum subarray prolem
#empty array is not included
arr=[-1,-2,3,5,4,-1,-10,-15,-20]

max_sum=sum=arr[0]
for i in range(1,len(arr)):
    sum+=arr[i]
    sum=max(sum,arr[i])
    max_sum=max(max_sum,sum)
print(max_sum)


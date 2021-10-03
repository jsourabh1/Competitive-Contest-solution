# onjective:- To find the largest power of any number
# idea:- is to divide the power int the power of two using the bianry number like
# 2^10 we can write 10=1010 in the binary so we can divide the power in two 2^8.2^2 so totally we have to perform 
# the logn multiplications O(logn) instead of O(n)

# recursive solution :


def solve(number,power):

	if power==0:
		return 1

	temp=solve(number,power>>1)

	if power%2==0:
		return temp*temp
	else:
		return temp*temp*number

print(solve(2,80))


# iterative solution:
def solve():
	temp=1
	number=2
	power=80

	while power>0:

		if power%2:
			temp*=number

		number=number*number
		power//=2
	print(temp)


#solution with mod:

def solve():
	temp=1
	number=2%1000000007
	power=8

	while power>0:

		if power%2:
			temp*=number%1000000007

		number=number*number%1000000007
		power//=2

	print(temp)

solve()



# Apllications:

# calculate the particular fibonacci number


def solve(n):

	f=[[1,1],[1,0]]

	power(f,n)

	return f[0][0]


def multiply(f,m):

	first=f[0][0]*m[0][0]+f[0][1]*m[1][0]
	second=f[0][0]*m[0][1]+f[0][1]*m[1][1]
	third=f[1][0]*m[0][0]+f[1][1]*m[1][0]
	forth=f[1][0]*m[0][1]+f[1][1]*m[1][1]


	f[0][0]=first
	f[0][1]=second
	f[1][0]=third
	f[1][1]=forth
	# print(f)
	


def power(f,n):

	if n==0 or n==1:
		return 

	m=[[1,1],[1,0]]

	power(f,n//2)
	multiply(f,f)
	if n%2!=0:
		multiply(f,m)
	print(f)

print(solve(8))



# first problem MODX and second problem BIGMOD


for i in range(int(input())):

	number,power,mod=map(int,input().split())

	ans=1
	# print(mod)

	number=number%mod

	while power>0:

		if power%2:

			ans=(ans*number)%mod

		number=(number*number)%mod
		power//=2

	print(ans)



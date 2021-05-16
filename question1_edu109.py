#question link:-https://codeforces.com/contest/1525/problem/A
'''
You have an initially empty cauldron, and you want to brew a potion in it. The potion consists of two ingredients: magic essence and water. The potion you want to brew should contain exactly k % magic essence and (100−k) % water.

In one step, you can pour either one liter of magic essence or one liter of water into the cauldron. What is the minimum number of steps to brew a potion? You don't care about the total volume of the potion, only about the ratio between magic essence and water in it.

A small reminder: if you pour e liters of essence and w liters of water (e+w>0) into the cauldron, then it contains ee+w⋅100 % (without rounding) magic essence and we+w⋅100 % water.

'''


from math import gcd
for _ in range(int(input())):
	n=int(input())

	first=n
	second=100-n

	if n==0 or n==100:

		print(1)
		 
	else:

		num=gcd(first,second)

		while num!=1:

			first=first//num
			second=second//num
			
			num=gcd(first,second)

		print(first+second)
		
 
 
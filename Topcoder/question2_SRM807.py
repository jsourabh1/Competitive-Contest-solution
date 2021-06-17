class ContainsItsAverage:


	def missing(self,arr):


		summ=sum(arr)

		n=len(arr)+1

		ans=[]

		for i in arr:

			 temp=(n*i)-summ

			 ans.append(temp)

		return sorted(set(ans))



obj=ContainsItsAverage()
print(obj.missing([1,10,1000,100]))



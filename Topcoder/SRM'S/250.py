class CoolPairsEasy:

	def count(self,firstname,lastname):
		count1=0

		for i in range(len(lastname)):
			for j in range(len(lastname)):
				if i!=j and lastname[j]==firstname[i]:
					count1+=1
			
		return count1


do=CoolPairsEasy()
firstname=("james", "taylor")
lastname=("taylor", "james")
print(do.count(firstname,lastname))

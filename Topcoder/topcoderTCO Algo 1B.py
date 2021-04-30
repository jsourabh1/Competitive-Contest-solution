class HIndex:

	def cheat(self,real,budget,fake):

		real=list(real)
		real.sort(reverse=True)

		can_buy=budget//fake

		for i in range(len(real),0,-1):


			#print(i)
			#print("minimum",min(real[:i]))

			if min(real[:i])>=i:
				return i

			else:

				req=0
				for j in real[:i]:
					if j<i:
						req+=(i-j)

				#print("required",req)
				
				#print("can_buy",can_buy)
				if req<=can_buy:
					return i
		return 0


real=[25, 3, 5, 3, 8, 0]

budget=1447
fake=1000

root=HIndex()
print(root.cheat(real,budget,fake))
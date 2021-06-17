class HangmanHelper:


	def show(self,secret,letter):

		ans=""

		for i in secret:

			if i in letter:
				ans+=i
			else:
				ans+="_"

		return ans
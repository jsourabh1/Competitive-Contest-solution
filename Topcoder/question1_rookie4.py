from collections import Counter
class MarblePicking:

	def fewestColors(self,marbles,count):
		string=""
		for i in marbles:
			string+=i

		dict_1=Counter(list(map(str,string.strip())))
		c=0
		print(dict_1)
		for i in sorted(dict_1.values(),reverse=True):

			if count<=0:
				break
			count-=i
			c+=1
		return c

arr=("AABBCC")
root=MarblePicking()
print(root.fewestColors(arr,3))
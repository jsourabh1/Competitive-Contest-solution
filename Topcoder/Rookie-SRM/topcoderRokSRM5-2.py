#DaRk Developer


Topcoder Rookie SRM-8
Date-14/05/2021

Question:-

Problem Statement
    
You are given a string cards, where each character represents the color of a card. You then select two of those cards at random. Return the probability that they are the same color.

    

Limits
    
Time limit (s):
2.000
Memory limit (MB):
256
Notes
-
A return value that is less than 1e-9 absolute or relative error is considered correct.
Constraints
-
cards will contain between 2 and 50 characters, inclusive.
-
Each character of cards will be between 'A' and 'Z', inclusive.
Examples
0)

    
"AAB"
Returns: 0.3333333333333333
There are three ways to pick two cards, one of which is both "A" cards.
1)

    
"ABC"
Returns: 0.0
Can't get two the same when there's only one of each.
2)

    
"AA"
Returns: 1.0
Only two cards to choose, so we always get a matched pair.
3)

    
"ABABA"
Returns: 0.4

This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder,
 Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
Solution:-

from collections import Counter
class PickTwoCards:

	def equalProbability(self,cards):

		dict_1=Counter(cards)

		ans=0

		for i in dict_1.values():

			if i>=2:
				
		
				first=float(i)/float(len(cards))
				second=float((i-1))/float((len(cards)-1))
				
				ans+=first*second
		return float(ans)
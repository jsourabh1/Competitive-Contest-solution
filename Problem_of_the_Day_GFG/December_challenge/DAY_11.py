class Solution:

    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self, a, N):
        #Your code here
        dict_1 = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []

        def helper(arr, string, index):

            nonlocal N, ans

            if index == N:
                ans.append(string)
                return

            for i in arr[index]:

                helper(arr, string + i, index + 1)

        arr = []

        for i in a:
            arr.append(dict_1[i])

        helper(arr, "", 0)
        return ans


obj=Solution()
obj.possibleWords([2,3,4],3)
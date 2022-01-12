class Solution(object):
    def lengthOfLastWord(self, s):
        arr = s.strip().split(' ')
        return len(arr[len(arr)-1])
            


sol = Solution()
print(sol.lengthOfLastWord("sss sss "))

class Solution(object):
    def maxSubArray(self, nums):
        nowSum = 0
        maxSum = nums[0]
        for right in range(len(nums)):
            nowSum += nums[right]
            if nowSum > maxSum:
                maxSum = nowSum
            if nowSum < 0:
                nowSum = 0

        return maxSum
            


sol = Solution()
print(sol.maxSubArray([-2,1]))

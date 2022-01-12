class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        idx = 1
        for i in range(0, m):
            if i == 0:
                continue

            while idx < m and nums1[i-1] > nums1[idx]:
                idx += 1
            nums1[i] = nums1[idx]
            idx += 1
        
        idx = 1
        for i in range(m, m+n):
            if i == m:
                nums1[i] = nums2[i-m]
                continue

            while idx < n and nums2[i-m-1] > nums2[idx]:
                idx += 1
            nums1[i] = nums2[idx]
            idx += 1
        
        nums1.sort()
        

sol = Solution()
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)
# print(sol.merge([1], 1, [], 0))

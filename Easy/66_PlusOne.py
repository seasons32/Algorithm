def plusOneByIdx(digits, idx):
    if idx < 0:
        digits.insert(0,1)
        return digits
    elif digits[idx] == 9:
        digits[idx] = 0
        return plusOneByIdx(digits, idx-1)
    else:
        digits[idx] += 1
        return digits

class Solution(object):
    def plusOne(self, digits):
        return plusOneByIdx(digits, len(digits)-1)
        


sol = Solution()
print(sol.plusOne([1,9]))

class Solution(object):
    def addBinary(self, a, b):
        aNum = int('0b'+a, 2)
        bNum = int('0b'+b, 2)
        return str(bin(aNum + bNum)).replace("0b","")

        


sol = Solution()
print(sol.addBinary("1010", "1011"))

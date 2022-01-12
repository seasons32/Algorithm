stairs = [0 for col in range(46)]

def climbCnt(rem):
    if stairs[rem] > 0:
        return stairs[rem]

    stairs[rem] = climbCnt(rem-1) + climbCnt(rem-2)
    return stairs[rem]

class Solution(object):
    def climbStairs(self, n):
        stairs[1] = 1
        stairs[2] = 2
        stairs[3] = 3
        return climbCnt(n)
            
        


sol = Solution()
print(sol.climbStairs(3))


class Solution(object):
    def twoSum2(self, nums: list, target: int) -> list:
        k = len(nums) - 1
        i = 0
        res = []
        while i < k:
            if nums[i] + nums[k] > target:
                k -= 1
            elif nums[i] + nums[k] < target:
                i += 1
            else:
                res = [i, k]
                break
        return res
    
    def sortColors(self, nums: list) -> list:
        n = len(nums)
        p1 = 0
        p2 = n-1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            i += 1
        return nums




so = Solution()
# res = so.twoSum2([2,7,22,23], 9)
res = so.sortColors([0,1,2,1,2,0,1,2,0])
print(res)
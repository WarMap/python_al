
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

so = Solution()
res = so.twoSum2([2,7,22,23], 9)
print(res)
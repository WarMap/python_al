class Solution:
    def twoSum(self, nums: list, k: int):
        dic = {}
        for num in nums:
            key = k-num
            if num in dic:
                return [dic[num], num]
            else:
                dic[key] = num
    def twoSumIndex(self, nums: list, k: int):
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            key = k-num
            if num in dic:
                return [dic[num], i]
            else:
                dic[key] = i        

        
        
res = Solution()
r = res.twoSumIndex([2,7,11,15], 9)
print(r)
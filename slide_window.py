from collections import defaultdict, OrderedDict


# 滑动窗口
# 1. start/end 窗口的起始位置
# 2. lookup有默认值字典  
#     1. 0/1 有无    （最长不重复子串，只需知道包不包含；
#     2. -1/0/1 有多少  （覆盖目标串，包含几个了
#     3. 有时可简化， 比如数字和，不需要知道组成这个和的元素分别是什么，只记录一个和就可以
# 3. 目标结果 （当前遍历到的元素产生的满足条件目标结果，不一定是最终结果
# 4. 辅助的判断条件
#     1. 不重复子串，counter（有没有重复
#     2. 最小和子串，cur_val (当前子串和
#     3. 最短覆盖子串， counter（当前多少字符没覆盖



class Solution:

    def longestSubString(self, s: str) -> int:
        if not s: return 0
        max_len = start = end = counter = 0
        lookup = defaultdict(int)

        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end-start)
        return max_len

    def shortestSubArray(self, nums: list, target: int) -> int:
        if not nums: return 0
        start = end = curr = 0
        cur_val = 0
        min_val = float('inf')
        while end < len(nums):
            #  < target , 右边一直前进
            curr += nums[end]
            end += 1
            while curr >= target:
                curr -= nums[start]
                if curr < target:
                    min_val = min(min_val, end-start)
                start += 1
                
        return min_val

    def shortestCover(self, s: str, t: str) -> str:
        if not s: return None
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        start = end = 0
        counter = len(t)
        res = ""
        min_len = float("inf")
        while end < len(s):
            if target[s[end]] > 0:
                counter -= 1
            target[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > (end-start):
                    min_len = end-start
                    res = s[start: end]
                if target[s[start]] == 0:
                    counter += 1
                target[s[start]] += 1
                start += 1
        return res
            

so = Solution()
# k = so.longestSubString('ababcdecd')
# k = so.shortestSubArray([1,4,4], 4)
res = so.shortestCover('adobecodebanc', 'abc')
print(res)

# sol = Solution()

# result = sol.bytesCount(3)

# print(result)
# print(sol.isPowerOfTwo(8))
# print(sol.bytecount(4))
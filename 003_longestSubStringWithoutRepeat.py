
# 滑动窗口


class Solution(object):
    
    def longestSubString(self, s: str) -> int:
        if not s: return 0

        n = len(s)
        left = cur_len = max_len = 0
        lookup = set()

        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])        
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])

        return max_len

    def longestBan(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = end = max_len = counter = 0
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




so = Solution()
max_len = so.longestBan('aabcdeabd')
print(max_len)
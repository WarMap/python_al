from typing import DefaultDict, List

# n & n-1 移除二进制最后一位1
# n & 1 = 1 为奇 = 0 为偶


class Solution:

    def isPowerOfTwo(self, n):
        return n > 0 and not (n & n-1)

    def bytesCount(self, n):
        count = [0 for _ in range(0, n+1)]
        for i in range(1, n+1):
            count[i] = count[i & i-1] + 1
        return count

    def bytecount(self, n):
        res = 0
        while n != 0:
            n = n & n-1
            res += 1
        return res 


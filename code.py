import heapq

class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if a == INT_MIN and b == -1:
            return INT_MAX
        
        sign = -1 if (a > 0) ^ (b > 0) else 1
        
        a, b = abs(a), abs(b)
        ans = 0
        for i in range(31, -1, -1):
            if (a >> i) - b >= 0:
                a = a - (b << i)
                ans += 1 << i
        
        # bug 修复：因为不能使用乘号，所以将乘号换成三目运算符
        return ans if sign == 1 else -ans

    def isValidPara(self, s):
        stack = []
        paren_map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():
                return False
        return not stack


class MyQueue:
    def __init__(self):
        """
        initialize your data
        """
        self.s1 = []
        self.s2 = []
        self.front = None
    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)  

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.front = None
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self) -> None:
        if not self.s2 and not self.s1:
            return True
        return False


# class KthLargest:

#     def __init__(self, k, nums):
#         self.k = k
#         self.nums = nums
#         heapq.heapify(self.nums)

#     def add(self, val):
#         heapq.heappush(self.nums, val)
#         while len(self.nums) > self.k:
#             heapq.heappop(self.nums)
#         return self.nums[0]
class Heap:
    def __init__(self, desc=False):
        self.heap = []
        self.desc = desc

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _topper(self, i, j):
        return self.heap[i] < self.heap[j] if not self.desc else self.heap[j] < self.heap[i] 

    def _shift_up(self, index:int):
        """
        最后的元素找到合适的位置
        """
        while index:  #数组做bool
            parent = (index-1) // 2
            if self._topper(index, parent):
                self._swap(index, parent)
                index = parent
            else:
                break
    
    # def _shift_down(self):  加个index更通用
    #     """
    #     堆顶元素找到合适的位置
    #     """
    #     index = 0     尽量少些特例，尽量通用
    #     left =  1
    #     right = 2
    #     while left < len(self.heap):
    #         smaller = index
    #         if _topper(left, index):
    #             smaller = left
    #         elif right < len(self.heap) and _topper(right, index):
    #             smaller = right
    #         else 
    #             break
    #         _swap(smaller, index)
    #         index = smaller

    @property
    def size(self):
        return len(self.heap)

    def _shift_down(self, index):
        """
        堆顶元素找到合适的位置
        """
        while index*2+1 < self.size:
            left = index*2+1
            right = index*2+2

            smaller = index
            if self._topper(left, index):
                smaller = left
            elif right < self.size and self._topper(right, index):
                smaller = right
            else:
                break
            self._swap(smaller, index)
            index = smaller


    def push(self, val):
        self.heap.append(val)
        self._shift_up(self.size-1)

    def top(self):
        if self.size:
            return self.heap[0]
        return None

    def pop(self):
        topper = self.top
        self._swap(0, self.size-1)
        self.heap.pop()
        self._shift_down(0)
        return topper

# class Heap:
#     def __init__(self,desc=False):
#         """
#         初始化，默认创建一个小顶堆
#         """
#         self.heap = []
#         self.desc = desc
    
#     @property
#     def size(self):
#         return len(self.heap)
    
#     def top(self):
#         if self.size:
#             return self.heap[0]
#         return None
    
#     def push(self,item):
#         """
#         添加元素
#         第一步，把元素加入到数组末尾
#         第二步，把末尾元素向上调整
#         """
#         self.heap.append(item)
#         self._sift_up(self.size-1)
    
#     def pop(self):
#         """
#         弹出堆顶
#         第一步，记录堆顶元素的值
#         第二步，交换堆顶元素与末尾元素
#         第三步，删除数组末尾元素
#         第四步，新的堆顶元素向下调整
#         第五步，返回答案
#         """
#         item = self.heap[0]
#         self._swap(0,self.size-1)
#         self.heap.pop()
#         self._sift_down(0)
#         return item
    
#     def _smaller(self,lhs,rhs):
#         return lhs > rhs if self.desc else lhs < rhs
    
#     def _sift_up(self,index):
#         """
#         向上调整
#         如果父节点和当前节点满足交换的关系
#         （对于小顶堆是父节点元素更大，对于大顶堆是父节点更小），
#         则持续将当前节点向上调整
#         """
#         while index:
#             parent = (index-1) // 2
            
#             if self._smaller(self.heap[parent],self.heap[index]):
#                 break
                
#             self._swap(parent,index)
#             index = parent
    
#     def _sift_down(self,index):
#         """
#         向下调整
#         如果子节点和当前节点满足交换的关系
#         （对于小顶堆是子节点元素更小，对于大顶堆是子节点更大），
#         则持续将当前节点向下调整
#         """
#         # 若存在子节点
#         while index*2+1 < self.size:
#             smallest = index
#             left = index*2+1
#             right = index*2+2
            
#             if self._smaller(self.heap[left],self.heap[smallest]):
#                 smallest = left
                
#             if right < self.size and self._smaller(self.heap[right],self.heap[smallest]):
#                 smallest = right
                
#             if smallest == index:
#                 break
            
#             self._swap(index,smallest)
#             index = smallest
    
#     def _swap(self,i,j):
#         self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

class KthLargest:

    def __init__(self, k: int, nums:[int]):
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.heap.push(num)
            if self.heap.size > k:
                self.heap.pop()


    def add(self, val: int) -> int:
        self.heap.push(val)
        if self.heap.size > self.k:
            self.heap.pop()
        return self.heap.top()


# k = KthLargest(3, [4,5,8,2])
# print(k.add(3))
# print(k.add(5))
# print(k.add(10))
# s = Solution()
# res = s.divide(20, 6)
# print(res)
# print(s.isValidPara('()'))

h = Heap()
h.push(3)
h.push(5)
h.push(6)
h.push(4)
h.push(2)
h.push(1)
print(h.heap)
from ListNode import ListNode

# 非空链表
# 逆序存储
# 非负整数
# 除0，不会以0开头

class Solution(object):
    
    def addTwoNumbers(self, l1, l2) -> ListNode:
        carry = 0
        head = curr = ListNode(0)
        while l1 or l2:
            tmp = carry
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            carry = tmp // 10
            curr.next = ListNode(tmp % 10)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next

so = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

res = so.addTwoNumbers(l1, l2)
print(res)
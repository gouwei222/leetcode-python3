# # #K个一组翻转链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create_linked_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution(object):
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        res=[]
        #先将所有的节点存在数组中
        while head:
            res.append(head)
            head=head.next
        n=len(res)
        #如果k大于节点数，直接返回初始节点
        if k>n:
            return res[0]
        #依次将数组中左右指针间的k个节点翻转
        left,right=0,k
        while right<=n:
            res2=res[left:right]
            res2.reverse()
            res[left:right]=res2
            left+=k
            right+=k
        #翻转后的节点重新连接
        for i in range(n-1):
            res[i].next=res[i+1]
        res[-1].next=None
        return res[0]

# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         def rev(a, b):  # 指定区间反转，到b结束
#             p, c = None, a
#             while c != b:
#                 t = c.next
#                 c.next = p
#                 p, c = c, t
#             return p
#
#         a = b = head  # 初始化 头结点，a之后为反转子链表的尾结点
#         for i in range(k):  # 找到k节点之后的节点
#             if not b: return head
#             b = b.next
#         n = rev(a, b)  # 反转a-b区间的k个节点
#         a.next = self.reverseKGroup(b, k)  # 递归更新尾节点的指针
#         return n



if __name__ == "__main__":
    head1 = create_linked_list([1, 2, 3, 4, 5])
    a = Solution()
    print(a.reverseKGroup(head1,2))





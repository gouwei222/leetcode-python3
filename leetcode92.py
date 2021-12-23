#反转链表2
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


class Solution:
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next  # 反转
            cur.next = pre  #
            pre = cur  # 移位
            cur = tmp  #
        return pre
        ##标准的反转链表

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return []
        dummy = cur = ListNode(-1)
        cur.next = head
        # for _ in range(left-1):
        #     cur=cur.next#左边

        # right_node=cur#初始化的右边跟左边一样
        # for _ in range(right-left+1):
        #     right_node=right_node.next
        # #切断一个子链表
        # left_node=cur.next #左边
        # curr=right_node.next#存右边

        # cur.next=None
        # right_node.next=None

        # self.reverse(left_node)
        # cur.next=right_node#拼回去
        # left_node.next=curr
        # return dummy.next
        for _ in range(left - 1):
            cur = cur.next
        l, lt = cur, cur.next  # 存反转的头节点跟下一个节点
        for _ in range(right - left + 1):
            cur = cur.next

        r, cur.next = cur.next, None
        l.next = self.reverse(l)
        lt.next = r
        return dummy.nextde  # 拼回去
        left_node.next = curr
        return dummy.next


if __name__ == "__main__":
    head1 = create_linked_list([1, 2, 3, 4, 5])
    a = Solution()
    print(a.reverseBetween([1,2,3,4,5],2,4))


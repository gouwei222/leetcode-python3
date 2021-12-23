class Solution:
    def isPalindrome(self, s):
        ret = ""
        for i in s:
            if i.isalnum():
                ret=ret+(i.lower())   #字符串没有append用法，就得按照下面用join这样子写
        # ret = "".join(i.lower() for i in s if i.isalnum())
        n=len(ret)
        left,right=0,n-1
        while(left<=right):
            if ret[left]!=ret[right]:
                return False
            left+=1
            right-=1
        return True



a=Solution()
print(a.isPalindrome("race a car"))
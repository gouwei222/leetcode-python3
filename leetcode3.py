#无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if (not s): return 0
        left, right, res = 0, 0, 0
        # hash_set = set()
        while(right<len(s)):
            while s[right] in s[left:right]: #####s[left:right]取不到s[right]这一个
                left +=1
            res = max(res, right-left+1)
            right +=1
        return res
a=Solution()
print(a.lengthOfLongestSubstring("abcabccc"))
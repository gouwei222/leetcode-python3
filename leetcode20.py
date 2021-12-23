#有效的括号
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 == 1:
#             return False
#
#         pairs = {
#             ")": "(",
#             "]": "[",
#             "}": "{",
#         }
#         stack = list()
#         for ch in s:
#             if ch in pairs:
#                 if not stack or stack[-1] != pairs[ch]:
#                     return False
#                 stack.pop()
#             else:
#                 stack.append(ch)
#
#         return not stack

#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         brackets = {')': '(', '}': '{', ']': '['}
#         stack = []
#         for i in s:
#             if not stack:
#                 stack.append(i)
#             elif stack[-1] == brackets.get(i):
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return False if stack else True

#replace也可以，python好快乐呀
# class Solution:
#     def isValid(self, s: str) -> bool:
#         for i in ('()','[]','{}')*(len(s)//2):
#           s=s.replace(i,'')
#         return not bool(s)

class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2==1:
            return False
        stack=[]
        dic={')':'(',
             ']':'[',
             '}':'{'
             }

        for ch in s:
            # if stack and ch in dic:
            #     if stack[-1]==dic[ch]:
            #         stack.pop()
            #     else:
            #         return False
            # else:
            #     stack.append(ch)
            if not stack:
                stack.append(ch)

            elif stack[-1]==dic.get(ch):
                stack.pop()
            else:
                stack.append(ch)

        return not stack

a=Solution()
print(a.isValid("([])"))



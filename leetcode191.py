class Solution:
    def hammingWeight(self, n: int) -> int:#n是个整型，没有len0
        # l=len(n)
        return bin(n).count('1')
a=Solution()
print(a.hammingWeight(0b0000000000000000000000000001011))
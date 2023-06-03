class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list=[]
        result=[]
        for i in range(len(nums)):
            list.append(int(nums[i]))
        s=sorted(list,reverse=True)
        for j in range(len(s)):
            result.append(str(s[j]))
        return result[k-1]

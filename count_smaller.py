class Solution:
    def smallerNumbersThanCurrent(self, nums):
        size=len(nums)
        final=[0]*size
        for i in range(size):
            for j in range(size):
                if i!=j and  nums[i] >nums[j]:
                    final[i] +=1

        return final

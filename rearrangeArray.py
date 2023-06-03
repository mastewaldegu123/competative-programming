class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[]
        array=sorted(nums)
        count=1
        x=int(len(nums)/2)
       
        for i in range(len(nums)):
            if i<=x:
                result.append(array[i])
            else:
                result.insert(count,array[i])
                count +=2
        return result

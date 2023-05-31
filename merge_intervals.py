class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[intervals[0]]
        for x,y in intervals[1:]:
            lastValue=result[-1][1]
            if x<=lastValue:
                result[-1][1]=max(lastValue,y)
            else:
                result.append([x,y])
        return result
            

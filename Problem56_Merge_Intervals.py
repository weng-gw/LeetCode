class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=out[-1][1]:
                out[-1][1] = max(intervals[i][1],out[-1][1])
            else:
                out.append(intervals[i])
        return out

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []
        prev = -1

        for start, end in intervals:
            if prev < start:
                res.append([start, end])
                prev = end
            elif prev >= start and end > prev:
                res[-1] = [res[-1][0], end]
                prev = end

        return res

        
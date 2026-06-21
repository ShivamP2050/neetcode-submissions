class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        arr.sort()
        res = []
        while k > 0:
            snip = arr.pop()
            res.append(snip[1])
            k -= 1
        return res
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(x, y)
            print(stones)
            z = x - y
            if z > 0:
                heapq.heappush_max(stones, z)

        if stones:
            return stones[0]
        print(stones)
        return 0
        
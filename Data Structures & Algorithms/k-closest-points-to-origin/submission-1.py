class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            dist = ((x)**2 + (y)**2)
            heap.append((dist, x, y))

        heapq.heapify(heap)
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res

        
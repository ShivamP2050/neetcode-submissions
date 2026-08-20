class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []

        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            distances.append((dist, point))

        heapq.heapify(distances)
        for i in range(k):
            if distances:
                res.append(heapq.heappop(distances)[1])
            else:
                break

        return res


        
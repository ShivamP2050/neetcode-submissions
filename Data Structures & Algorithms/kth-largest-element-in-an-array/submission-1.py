class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums
        heapq.heapify_max(maxHeap)
        res = nums[0]
        for i in range(k):
            res = heapq.heappop_max(maxHeap)
        return res
        
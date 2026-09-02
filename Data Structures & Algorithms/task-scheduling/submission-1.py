from collections import defaultdict
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = defaultdict(int)
        for i in tasks:
            counter[i] += 1

        counts = list(counter.values())
        heapq.heapify_max(counts)
        queue = deque()
        
        while counts or queue:
            time += 1
            if counts:
                val = heapq.heappop_max(counts)
                if val > 1:
                    queue.append((val - 1, time + n))

            if queue:
                if queue[0][1] <= time:
                    add = queue.popleft()[0]
                    heapq.heappush_max(counts, add)                
        
        return time
                
        
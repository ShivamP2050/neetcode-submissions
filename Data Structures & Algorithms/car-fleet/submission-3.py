class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, velocity = zip(*sorted(zip(position, speed)))

        time = 0
        count = 0
        for i in range(len(position) - 1, -1, -1):
            current_time = (target - position[i]) / velocity[i]
            if time < current_time:
                count += 1
                time = current_time
        
        return count


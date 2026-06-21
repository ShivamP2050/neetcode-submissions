class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            if i > 0 or not res or res[-1] < 0:
                res.append(i)
            else:
                while res and res[-1] > 0 and res[-1] < -1 * i:
                    res.pop()
                if res and res[-1] == -1 * i:
                    res.pop()
                    continue
                if not res or res[-1] < 0:
                    res.append(i)
        return res

        
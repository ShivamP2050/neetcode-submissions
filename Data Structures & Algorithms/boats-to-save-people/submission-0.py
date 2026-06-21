class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        r = len(people) - 1
        l = 0
        res = 0
        people.sort()

        while l <= r:
            if people[r] + people[l] <= limit:
                res += 1
                r -= 1
                l += 1
            else:
                res += 1
                r -= 1
        
        return res
        
class StockSpanner:

    def __init__(self):
        self.span = []
        

    def next(self, price: int) -> int:
        count = 1
        i = len(self.span) - 1
        while i >= 0 and self.span[i] <= price:
            count += 1
            i -= 1
        self.span.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class MedianFinder:

    def __init__(self):
        self.right_half = []
        self.left_half = []
        heapq.heapify(self.right_half)
        heapq.heapify(self.left_half)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right_half, num)
        if len(self.right_half) > len(self.left_half) + 1:
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))
        
        # resort which one is the left_half max, and right_half min!
        if len(self.left_half) > 0 and -self.left_half[0] > self.right_half[0]:
            cur_left_max = -heapq.heappop(self.left_half)
            cur_right_min = heapq.heappop(self.right_half)

            heapq.heappush(self.left_half, -cur_right_min)
            heapq.heappush(self.right_half, cur_left_max)

    def findMedian(self) -> float:
        if (len(self.left_half) + len(self.right_half)) % 2 == 0:
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return self.right_half[0]
        
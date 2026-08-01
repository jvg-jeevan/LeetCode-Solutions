import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # here sorting based on the closest distance using lambda function
        # points.sort(key = lambda point: point[0]**2 + point[1]**2)
        # return points[:k]

        # using minheap

        heap = []
        # calculate distance and push to minheap as python only supports maxheap push in -ve
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
        
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
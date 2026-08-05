class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        cls = {}
        for point in points:
            x = point[0]
            y = point[1]
            if len(cls) < k:
                cls[(x,y)] = math.sqrt((x ** 2) + (y ** 2))
            else:
                dis = math.sqrt((x ** 2) + (y ** 2))
                if dis < max(cls.values()):
                    max_key = max(cls, key=cls.get)
                    del cls[max_key]
                    cls[(x,y)] = dis
        return list(map(lambda x: [x[0], x[1]], cls.keys()))
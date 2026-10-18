class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        res = ""

        cur = self.hm.get(key, [])

        l, r = 0, len(cur) - 1

        while l <= r:
            m = (l + r) // 2
            ts, val = cur[m]
            if ts < timestamp:
                res = val
                l = m + 1
            elif ts == timestamp:
                return val
            else:
                r = m - 1
        return res


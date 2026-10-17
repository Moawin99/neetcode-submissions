class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = []
        self.tm[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        
        res = ""

        ele = self.tm.get(key, [])

        l, r = 0, len(ele) - 1

        while l <= r:
            m = (l + r) // 2
            ts, val = ele[m]
            if timestamp > ts:
                res = val
                l = m + 1
            elif timestamp < ts:
                r = m - 1
            else:
                return val
        return res

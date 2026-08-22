class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        # base case
        if key not in self.times:
            return ""

        timestamps = self.times[key]
        values = self.values[key]

        l, r = 0, len(timestamps) - 1
        res = -1

        while l <= r: # situations where there is only one value values: [1]
            mid = (l + r) // 2
            if timestamps[mid] <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        if res == -1:
            return ""
        else:
            return values[res]


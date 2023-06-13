class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        # print(self.store)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        #  in case get key isnot in self.store
        # print(timestamp,self.store[key][0][1])
        if key in self.store and  timestamp >= self.store[key][0][1]:
            values = self.store[key]
        else:
            values = []
            return ""
        # if key not in self.store or timestamp < self.mapping[key][0][0]:
        #     return ""
        # binary search
        l, r = 0, len(values) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if values[m][1] ==  timestamp:
                return values[m][0]
            if values[m][1] <  timestamp:
                l = m
            else:
                r = m 
        if values[r][1] <= timestamp:
            return values[r][0]
        return values[l][0]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

class TimeMap:

    def __init__(self):
        self.timemap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = {}
            self.timemap[key][timestamp] = value
        
        elif key in self.timemap:
            self.timemap[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        if timestamp not in self.timemap[key]:

            k = -1
            for i in range(timestamp, -1, -1):
                if i in self.timemap[key].keys():
                    k = i
                    break

            if k == -1:
                return ""

            return self.timemap[key][k]

        return self.timemap[key][timestamp]    



        
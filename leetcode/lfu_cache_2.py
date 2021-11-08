from collections import OrderedDict, defaultdict

#############
# sample 1161 ms submission
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyfreq = defaultdict(int)
        self.freqkey = defaultdict(OrderedDict)
        self.min_freq = None

    def get(self, key: int) -> int:
        if key in self.keyfreq:
            freq = self.keyfreq[key]
            val = self.freqkey[freq][key]
            self.freqkey[freq].pop(key)
            self.keyfreq[key] += 1
            self.freqkey[freq + 1][key] = val
            if len(self.freqkey[freq]) == 0:
                del self.freqkey[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.keyfreq:
            freq = self.keyfreq[key]
            self.freqkey[freq][key] = value
            self.get(key)
        else:
            if len(self.keyfreq) == self.capacity:
                del_key, del_val = self.freqkey[self.min_freq].popitem(last=False)
                del self.keyfreq[del_key]
            self.min_freq = 1
            self.freqkey[1][key] = value
            self.keyfreq[key] = 1
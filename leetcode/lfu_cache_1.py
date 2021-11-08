from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_counter = defaultdict(int)
        self.counter_dict = defaultdict(OrderedDict)
        self.min_freq = 1

    def get(self, key: int) -> int:
        if key not in self.key_counter:
            return -1

        freq = self.key_counter[key]
        value = self.counter_dict[freq][key]
        self.key_counter[key] += 1
        del self.counter_dict[freq][key]
        new_freq = self.key_counter[key]
        self.counter_dict[new_freq][key] = value
        self.counter_dict[new_freq].move_to_end(key)
        if freq == self.min_freq and not self.counter_dict[self.min_freq]:
            self.min_freq += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_counter:
            freq = self.key_counter[key]
            self.counter_dict[freq + 1][key] = value
            del self.counter_dict[freq][key]
            self.counter_dict[freq + 1].move_to_end(key)
            self.key_counter[key] = freq + 1
            if freq == self.min_freq and not self.counter_dict[self.min_freq]:
                self.min_freq += 1
            return

        elif len(self.key_counter) == self.capacity:
            if not self.key_counter:
                return
            rm_key, rm_v = self.counter_dict[self.min_freq].popitem(last=False)
            del self.key_counter[rm_key]

        freq = 1
        self.counter_dict[freq][key] = value
        self.key_counter[key] = freq
        self.min_freq = 1

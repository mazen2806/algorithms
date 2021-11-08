class LRUCache:
    """
    LRU(Least Recently Used) cache should only be used when user wants to reuse previously computed values
    """
    def __init__(self, capacity = 1):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.lr_keys = []

    def get(self, key) -> int:
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.lr_keys.remove(key)
            self.lr_keys.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.lr_keys.remove(key)
        self.cache[key] = value
        self.lr_keys.append(key)

        if len(self.cache) > self.capacity:
            del self.cache[self.lr_keys[0]]
            self.lr_keys = self.lr_keys[1:]


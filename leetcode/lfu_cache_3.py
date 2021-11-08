######
class DLinkedNode:
    def __init__(self, key, value):
        self.prev, self.next = None, None
        self.key, self.value = key, value
        self.freq = 1


class DLinkedList:
    def __init__(self):
        self.head, self.tail = DLinkedNode(0, 0), DLinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_from_tail(self):
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int):
        self.__freq = defaultdict(DLinkedList)
        self.__node = defaultdict(DLinkedNode)
        self.__capacity = capacity
        self.__min_freq = 0

    def update(self, key):
        node = self.__node[key]
        node_freq = node.freq
        self.__freq[node_freq].remove_node(node)
        if node_freq == self.__min_freq and self.__freq[self.__min_freq].size == 0:
            self.__min_freq += 1
        node.freq += 1
        self.__freq[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.__node:
            return -1
        val = self.__node[key].value
        self.update(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.__capacity == 0:
            return
        if key in self.__node:
            self.__node[key].value = value
            self.update(key)
        else:
            if len(self.__node) == self.__capacity:
                node = self.__freq[self.__min_freq].remove_from_tail()
                del self.__node[node.key]

            newNode = DLinkedNode(key, value)
            self.__min_freq = 1
            self.__freq[self.__min_freq].add_to_head(newNode)
            self.__node[key] = newNode

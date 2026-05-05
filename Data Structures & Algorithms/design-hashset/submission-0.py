class MyHashSet:

    def __init__(self):
        self.lst = [[] for _ in range(10000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.lst[key // 100].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.lst[key // 100].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.lst[key // 100]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
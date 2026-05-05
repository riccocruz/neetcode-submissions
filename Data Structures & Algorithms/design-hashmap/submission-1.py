class MyHashMap:

    def __init__(self):
        self.d = [[] for _ in range(10001)]

    def put(self, key: int, value: int) -> None:
        if len(self.d[key // 100]) == 0:
            self.d[key // 100].append((key, value))
            return 

        for i, item in enumerate(self.d[key // 100]):
            if item[0] == key:
                self.d[key // 100][i] = (key, value)
                return 
        self.d[key // 100].append((key, value))

    def get(self, key: int) -> int:
        print(self.d[key // 100])
        for item in self.d[key // 100]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        for i, (k, v) in enumerate(self.d[key // 100]):
            if k == key:
                self.d[key // 100].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
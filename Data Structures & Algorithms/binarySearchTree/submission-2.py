class TreeMap:
    
    def __init__(self):
        self.nodes = {}

    def insert(self, key: int, val: int) -> None:
        self.nodes[key] = val

    def get(self, key: int) -> int:
        if key in self.nodes:
            return self.nodes[key]
        return -1

    def getMin(self) -> int:
        if len(self.nodes) > 0:
            return self.nodes[sorted(self.nodes.keys())[0]]
        return -1

    def getMax(self) -> int:
        if len(self.nodes) > 0:
            return self.nodes[sorted(self.nodes.keys())[-1]]
        return -1

    def remove(self, key: int) -> None:
        if key in self.nodes:
            del self.nodes[key]
        return

    def getInorderKeys(self) -> List[int]:
        return sorted(self.nodes.keys())

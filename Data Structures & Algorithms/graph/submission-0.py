class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        start_node = self.adj_list[src]
        if dst in start_node:
            start_node.remove(dst)
            return True
        return False
        

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list or len(self.adj_list) == 0:
            return False
        queue = deque()
        visit = set()
        queue.append(src)
        visit.add(src)

        while queue:
            parent = queue.popleft()
            if dst in self.adj_list[parent]:
                return True
            for edge in self.adj_list[parent]:
                if edge not in visit:
                    queue.append(edge)
                    visit.add(edge)
        return False

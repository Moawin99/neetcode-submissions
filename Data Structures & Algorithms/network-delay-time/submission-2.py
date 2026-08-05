class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        
        for ui, vi, ti in times:
            adj[ui].append([ti, vi])
        
        shortest = {}
        minHeap = [[0, k]]
        time = 0
        while minHeap:
            cost, src = heapq.heappop(minHeap)

            if src in shortest:
                continue

            shortest[src] = cost
            time = cost
            for ti, vi in adj[src]:
                if vi not in shortest:
                    heapq.heappush(minHeap, [cost + ti, vi])
            
        return time if len(shortest) == n else -1

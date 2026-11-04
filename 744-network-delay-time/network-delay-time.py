import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue                      # stale entry
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        ans = max(dist[1:])
        return ans if ans != float('inf') else -1
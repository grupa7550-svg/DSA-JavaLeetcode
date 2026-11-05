class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            nxt = dist[:]                      # snapshot: only use last round's values
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < nxt[v]:
                    nxt[v] = dist[u] + w
            dist = nxt

        return dist[dst] if dist[dst] != INF else -1
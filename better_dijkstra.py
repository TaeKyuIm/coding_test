import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 우선순위 힙 자료구조 활용으로 시간 복잡도를 O(V^2)에서 O(ElogV)로 줄였다.

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start):
    q = [] # 큐를 활용할 리스트
    heapq.heappush(q, (0, start)) # (경로, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: # 처리된적 있는 노드면 그냥 생략
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 개정된 거리와 그 노드를 넣음
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])
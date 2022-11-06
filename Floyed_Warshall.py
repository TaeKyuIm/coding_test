INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0 # 자기자신은 최단거리 0으로 만듬

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # 점화식을 코드로 표현
            # 플로이드-워셜 알고리즘은 기본적으로 다이나믹 프로그래밍임.
            
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('Infinity', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
# 간단한 다익스트로 O(V^2) -> 전체 노드 개수 10000개 이상 넘어가면 안됨

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 거리 10억으로 설정

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드
graph = [[] for i in range(n+1)] # 노드 정보 담을 그래프 리스트 선언
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a노드에서 b노드 가는데 c만큼 비용 발생
    graph[a].append((b, c))

# 방문안한 노드중 가장 거리 짧은 노드 반환
def get_smallest_node():
    min_value = INF # 최소값 구하기 이므로 최대값으로 문제 시작
    index = 0 # 최단 거리 짧은 노드용 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작 노드 거리 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 거리 테이블에 걸리는 비용 넣어줌, j[0] : 목적지 노드 j[1] : 비용
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True # 최단거리가 가장 짧은 노드를 꺼내서 방문 처리
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])
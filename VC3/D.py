import heapq
N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))

heapq.heapify(A)


for _ in range(M):
    a = heapq.heappop(A)
    a = -(-a//2)
    heapq.heappush(A,a)

print(-1*sum(A))
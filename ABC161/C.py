N,K = list(map(int, input().split()))

print(min(K-N%K,N%K))
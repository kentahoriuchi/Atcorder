import math
N,M,K = list(map(int, input().split()))
 
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))%1000000007
 
print(comb(N*M-2,K-2)*M*N*(M*(N**2-1)+N*(M**2-1))//6%1000000007)
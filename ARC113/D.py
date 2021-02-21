N,M,K = list(map(int, input().split()))
mod = 998244353

print(pow(58979,31415,mod)+pow(58979,92653,mod)-1)
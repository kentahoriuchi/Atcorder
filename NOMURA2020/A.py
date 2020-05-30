H1,M1,H2,M2,K= list(map(int, input().split()))

a1 = H1*60+M1
a2 = H2*60+M2

print(a2-a1-K)
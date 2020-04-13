N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def kaijou(n):
    s = 1
    for i in range(n):
        s *= i+1
    return s

def jisyo(L):
    l = 0
    k = len(L)
    for i in range(k):
        n = L.pop(0)
        l += kaijou(len(L))*(n-1)
        for m in range(len(L)):
            if L[m] > n:
                L[m] -= 1
    return l+1

print(abs(jisyo(P)-jisyo(Q)))





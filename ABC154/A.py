S,T = list(input().split())
A,B = list(map(int, input().split()))
U = input()

if U == S:
    print('%d %d' %(A-1,B))
else:
    print('%d %d' %(A,B-1))


N,A,B = list(map(int, input().split()))


print(max((N-2)*B-(N-2)*A+1,0))
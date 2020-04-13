N = int(input())
A = list(map(int, input().split()))
count = 0
s = 0

while(True):
    for i in range(len(A)):
        s += A[i]%2
    
    if s != 0:
        break
    else:
        A = list(map(lambda x:x/2,A)) 
        count +=1

print(count)
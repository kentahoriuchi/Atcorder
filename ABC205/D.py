N,Q = list(map(int, input().split()))
A  = list(map(int, input().split()))
A.sort()

def search(i):
    left = 0
    right = N
    while left < right:
        mid = int((left + right)/2)
        if A[mid] == i:
            return -1 *(i - mid)
        elif A[mid] > i:
            right = mid
        else:
            left = mid + 1
    mid = int((left + right)/2)
    return i - mid

for i in range(Q):
    K = int(input())
    # print('aaaaaaaa',K)
    left = 0
    right = K+len(A)+1
    while left < right:
        mid = int((left + right)/2)

        # print(mid)
        # print(search(mid))
       
        l = search(mid)
        # print(mid,l)
        if l < 0:
            if -l <= K:
                right += 1
            else:
                left -= 1
        elif l == K:
            print(mid)
            break
        elif l > K:
            right = mid
        else:
            left = mid + 1

# print(search(4))
    

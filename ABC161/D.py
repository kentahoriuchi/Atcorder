from collections import deque

K = int(input())
if K <= 9:
    print(K)
else:
    que = deque([9,8,7,6,5,4,3,2,1])
    count = 0

    while True:
        x = que.pop()
        count += 1
        if count == K:
            break
        if x%10 != 0:
            que.appendleft(x*10+x%10-1)
        que.appendleft(x*10+x%10)
        if x%10 != 9:
            que.appendleft(x*10+x%10+1)
    
    




            

    print(x)
#JOI 2009 本選 2 - ピザ
 
d = int(input())
n = int(input())
m = int(input())
shop = [0,d,10000000000]
order = []
 
def search_shop(i):
    left = 0
    right = n + 1
    while left < right:
        mid = int((left + right)/2)
        if shop[mid] == i:
            return 0
        elif shop[mid] < i and shop[mid+1] > i:
            return min(abs(shop[mid] - i) , abs(shop[mid + 1] - i))
        elif shop[mid] < i:
            left = mid + 1
        else:
            right = mid
 
 
for i in range(1,n):
    k = int(input())
    shop.append(k)
for i in range(m):
    k = int(input())
    order.append(k)
shop = sorted(shop)
 
ans = 0
for i in order:
    ans += search_shop(i)
print(ans)
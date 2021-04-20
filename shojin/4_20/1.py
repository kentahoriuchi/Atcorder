n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

S.sort()
T.sort()

def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1       

ans = 0
for t in T:
    if binary_search(S,t) != -1:
        ans += 1

print(ans)

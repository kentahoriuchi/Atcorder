N = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0

while(True):
    a.sort()
    alice += a.pop(-1)
    if a == []:
        break
    a.sort()
    bob += a.pop(-1)
    if a == []:
        break

print(alice-bob)

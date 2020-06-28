D = int(input())
c = list(map(int, input().split()))
s = []
t = []
for _ in range(D):
  s.append(list(map(int, input().split())))
for _ in range(D):
  t.append(int(input()))


ans = 0
last_date = [0]*26
for day in range(D):
  contest = t[day]-1
  ans += s[day][contest]
  last_date[contest] = day+1
  for j in range(26):
    ans -= c[j] * (day+1 - last_date[j])

  print(ans)


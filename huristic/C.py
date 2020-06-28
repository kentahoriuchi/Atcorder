D = int(input())
c = list(map(int, input().split()))
s = []
t = []
for _ in range(D):
  s.append(list(map(int, input().split())))
for _ in range(D):
  t.append(int(input()))

M = int(input())
d = []
q = []
for _ in range(M):
  tmp = list(map(int, input().split()))
  d.append(tmp[0])
  q.append(tmp[1])

ans = 0
last_date = [[0]*26 for _ in range(D)]
for day in range(D):
  contest = t[day]-1
  ans += s[day][contest]
  if day != 0:
    for j in range(26):
      last_date[day][j] = last_date[day-1][j]
  last_date[day][contest] = day+1
  for j in range(26):
    ans -= c[j] * (day+1 - last_date[day][j])


for i in range(M):
  day = d[i]-1 
  mae_contest = t[day]-1
  contenst = q[i]-1
  ans -= s[day][mae_contest]
  ans += s[day][contest]
  t[d[i]-1] = q[i]
  for change_day in range(day,D):
    if t[change_day] == q[i]:
      break
    ans += c[contest] * (last_date[day][contest]-day+1)
  print(ans)




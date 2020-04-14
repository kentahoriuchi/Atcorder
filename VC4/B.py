S = list(input())

o_count = S.count('0')
i_count = S.count('1')

print(min(o_count,i_count)*2)
a = list(input())
b = list(input())
c = list(input())

#ab
def ketsugou(a,b):
    ab = ''
    if len(a) == len(b):
        for j in range(len(a)):
                    if a[j] == b[j] or a[j] == '?' or b[j] == '?':
                        if s[j] == '?':
                            s[j] = t[j]
                        elif t[j] == '?':
                            t[j] = s[j]
                        continue
                    else:
                        flag += 1
                        break
    if a == b:
        ab = a
    else:
        for i in range(1,min(len(a),len(b))):
            k = min(len(a),len(b))-i
            print(k)
            s = a[-k:]
            t = b[:k]
            print(len(s),len(t))
            flag = 0
            for j in range(len(s)):
                if s[j] == t[j] or s[j] == '?' or t[j] == '?':
                    if s[j] == '?':
                        s[j] = t[j]
                    elif t[j] == '?':
                        t[j] = s[j]
                    continue
                else:
                    flag += 1
                    break
            
            if flag == 0:
                print(s)
                ab = ''.join(a[:-k]) + ''.join(s) + ''.join(b[k:])
                break
        if ab == '':
            ab = ''.join(a)+''.join(b)

    return ''.join(ab)

ab = ketsugou(a,b)
ba = ketsugou(b,a)
ac = ketsugou(a,c)
ca = ketsugou(c,a)
bc = ketsugou(b,c)
cb = ketsugou(c,b)
print(ab,ba,bc)

abc = ketsugou(ab,c)
bac = ketsugou(ba,c)
acb = ketsugou(ac,b)
cab = ketsugou(ca,b)
bca = ketsugou(bc,a)
cba = ketsugou(cb,a)

print(min(len(abc),len(bac),len(acb),len(cab),len(bca),len(cba)))





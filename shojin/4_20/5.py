p = float(input())

import math

t = 1.5 * (math.log2(math.log(2)*p/1.5))
ans = t + p*(2**(-t/1.5))
if t < 0:
    print(p)
else:
    print(ans)
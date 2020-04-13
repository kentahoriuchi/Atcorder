_,*l=map(int,open(0).read().split());print("YNeos"[any((t+x+y)%2+(t<x+y)for t,x,y in zip(*[iter(l)]*3))::2])

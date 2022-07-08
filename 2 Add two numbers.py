def func(a,b):
    a.reverse()
    b.reverse()
    s = [(x + y) for (x,y) in zip(a,b)]
    print(s)

print(func([2,3,5],[4,5,3]))

def func(*args):
    a=sorted((args))
    return a
r=func(2,8,1,6,2,9)
temp = r[0]
for i in r[1:]:
    if i!=temp:
        print(i);
        break;
print(r)
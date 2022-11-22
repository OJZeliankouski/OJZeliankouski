a=[1,2,3,4,5,6,7,8,9]
r=9
d=9
b=1
x=1
for i in a:
    if i==b:
        print("*"*r,"+"*x,"*"*d)
        x+=2
        d-=1
        b+=1
        r-=1

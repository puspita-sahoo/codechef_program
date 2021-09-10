t=int(input())
for i in range(t):
    r=int(input())
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    # r=n*n
    d1=(((x2-x1)**2)+((y2-y1)**2))*0.5
    d2=(((x3-x1)**2)+((y3-y1)**2))*0.5
    d3=(((x2-x3)**2)+((y2-y3)**2))*0.5
    print(d1)
    print(d2)
    print(d3)
    if((d1<=r and d2<=r)or(d2<=r and d3<=r)or(d1<=r and d3<=r)):
        print("yes")
    else:
        print("no")



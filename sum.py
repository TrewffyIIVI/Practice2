t=int(input())
while t:
    a,b,c=map(int,input().split())
    if a+b==c:
        print('yes')
    elif b+c==a:
        print('yes')
    elif c+a==b:
        print('yes')
    else:
        print('no')
    t=t-1

#SOLVED

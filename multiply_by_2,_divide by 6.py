n=int(input())
for i in range(n):
    moves=0
    m=int(input())
    while m%6==0:
        m=m/6
        moves+=1
    while m%3==0:
        m=m/3
        moves+=2
    if m==1:
        print(moves)
    else:
        print(-1)

    #SOLVED
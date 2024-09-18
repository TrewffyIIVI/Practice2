for i in range(int(input())):
    n,k = map(int, input().split())
    a=list(map(int, input().split()))
    rem=[]
    
    for i in range(n):
        temp=a[i]%k
        if temp==0:
            temp=k
        rem.append([temp, i+1])
    rem.sort(reverse=True, key= lambda x:x[0])
    
    for i in range(n):
        print(rem[i][1], end=" ")
    print()

    #solved
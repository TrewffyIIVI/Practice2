for i in range(0, int(input())):
    a,b = map(int, input().split())
    if(a==0):
        if(b%2==0):
            print("YES")
        else:
            print("NO")
    else:
        sum = a*1+b*2
        if(sum%2==0):
            print("YES")
        else:
            print("NO")

#SOLVED

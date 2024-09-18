def solve(arr):
    if len(set(arr))!=len(arr):
        return 'NO'
    return 'YES'
 
 
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve(arr))

#SOLVED
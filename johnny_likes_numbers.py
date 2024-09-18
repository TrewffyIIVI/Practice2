n, k = map(int,input().split())
print(k - (n%k) + n)

#SOLVED

# Time limit exceeded:

n, k = map(int,input().split())
x = int() 
while x <= n:
    x += 1 
while x > n and x%k != 0:
    x += 1

print(x)









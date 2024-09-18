element = int(input())

for i in range(element):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    max_val = -1
    count = 1
    for j in range(1, n):
        if a[j] == a[j-1]:
            count += 1
            if count >= 3:
                max_val = a[j]
                break
        else:
            count = 1
 
    print(max_val)


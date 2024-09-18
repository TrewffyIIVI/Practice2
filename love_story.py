t = int(input())

for i in range(t):
    s = input()
    r = 'codeforces'
    diff = 0
    for i in range (10):
        if s[i] != r[i]:
            diff += 1
    print (diff)

    #SOLVED
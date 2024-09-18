b, e = input().split()
n = int(input()) % 4
if n & 1 == 0:
    print("undefined")
elif ("^>v<".index(e) - "^>v<".index(b)) % 4 == n:
    print("cw")
else:
    print("ccw")

#SOLVED

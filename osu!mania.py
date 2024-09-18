i = int(input())
 
for i in range(i):
    output = []
    li = []
    ti = int(input())
    for i in range(ti):
        i = input()
        li.append(i)
    for i in li:
        output.append(str(str(i).find("#") + 1))
    out = " ".join(reversed(output))
    print(out)

    #SOLVED
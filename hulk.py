n = int(input())
 
d = []
 
for i in range(1, n+1):
    if i%2==1:
        d.append("I hate")
    else:
        d.append("I love")
 
print(" that ".join(d) + " it")
 
#SOLVED
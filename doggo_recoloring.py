dogs =int(input())
row = input()
d = dict.fromkeys(row,0)


for i in range(dogs):
    d[row[i]]+=1
    if(d[row[i]])>1:
        print("YES");break
else:print('NO' if dogs!=1 else 'YES') 
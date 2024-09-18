games = int(input())
rounds_won = str(input())
D = rounds_won.count('D')
A = rounds_won.count("A")

if D > A:
    print("Danik")
elif A > D:
    print("Anton")
else:
    print("Friendship")
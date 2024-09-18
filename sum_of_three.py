for i in range(int(input())):
    integer = int(input())
    if integer == 9 or integer < 7:
        print('NO')
    else:
        print('YES')
        if integer % 3 == 0:
            print(1,4,(integer-5))
        else:
            print(1,2,(integer-3))


#SOLVED

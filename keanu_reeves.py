n= int(input())
matrix = input()[:n]

if n% 2 !=0:
	print(1)
	print(matrix)
else:
	if(matrix.count('1') != matrix.count('0')):
		print(1)
		print(matrix)
	else:
		print(2)
		print(matrix[:n-1], matrix[-1])


#SOLVED
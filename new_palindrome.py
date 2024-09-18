n = int(input())
for i in range(n):
	s = input()
	m = set()
	for i in range(len(s) // 2):
		m.add(s[i])
	if (len(m) == 1):
		print('NO')
	else:
		print('YES')

#SOLVED
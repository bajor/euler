sum = 0

for x in range(0, 1000):

	l = x // 100

	k = x % 100
	k = k // 10

	m = x % 10

	if (l + k + m) % 3 == 0 or m == 0 or m == 5:
		sum = sum + x

print sum
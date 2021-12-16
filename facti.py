def fact_rec(n):
	if n == 1 or n == 0:
		return 1
	return n * fact_rec(n-1)


print(fact_rec(5))

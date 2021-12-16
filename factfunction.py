def fact_iter(n):
	pro = 1
	for i in range(n):
		pro = pro * (i+1)
	return pro
print(fact_iter(5))

# recursive

def fact_rec(n):
	if n == 1 or n == 0:
		return 1
	return n * fact_rec(n-1)


print(fact_rec(5))


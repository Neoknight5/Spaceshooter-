#calculator
while True:
	val1 = int(input("enter your first value  :"))
	val2 = int(input("enter your second value: "))
	a = []
	b = []
	a.append(val1)
	b.append(val2)
	add = [(a+b)for a,b in zip(a,b)]
	print(f"this is your final :- {add}")
	print("_____________________")

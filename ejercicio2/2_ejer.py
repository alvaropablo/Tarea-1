def listaPares(a,b):
	nume=[]
	pares=[]
	for i in range(a,b+1):
		nume.append(i)
		if (i%2==0):
			pares.append(i)
	print(nume)
	print(pares)
listaPares(1,20)
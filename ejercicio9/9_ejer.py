def primo(n):
	if(n==1):
		return False
	centro=int(n/2)+1
	con=True
	for x in range(2,centro):
		if(n%x==0):
			return False
	return con
def sumPrimo(n):
	suma=0
	con=0
	con1=2
	while(con<n):
		if(primo(con1)):
			#print(con1)
			suma=suma+con1
			con=con+1
		con1=con1+1
	print(suma)
sumPrimo(4)
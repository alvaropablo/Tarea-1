def es_Palindromo(a):
	b=a[::-1]
	if (b==a):
		return True
	return False
print (es_Palindromo("radar"))
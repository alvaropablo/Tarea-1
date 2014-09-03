def numeroLetrasNum(n):
	num=0
	let=0
	for x in range(1,len(n)):
		if(n[x].isdigit()):
			num=num+1
		if(n[x].isalpha()):
			let=let+1
	print("hay: "+str(num)+" numeros")
	print("hay: "+str(let)+" letras")
numeroLetrasNum("¡Hola amigos! 12345")
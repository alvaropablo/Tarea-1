def valorCadena(a,b):
	if (len(a)==len(b)):
		print(a+b+"")
		return
	if (len(a)>len(b)):
		print(a)
	else:
		print(b)
valorCadena("hola","mundo")
valorCadena("pelota","casa")
valorCadena("Juan","Pepe")
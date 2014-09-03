import math

def triangulo(a,b,c):
	if(a+b>c or b+c>a or a+c>b):
		if(a==b==c):
			print("Triangulo equilatero")
			return
		if(a==b or b==c or c==a):
			print("triangulo isoceles")
			return
		if(math.sqrt(math.pow(a,2)+math.pow(b,2))==c or math.sqrt(math.pow(b,2)+math.pow(c,2))==a or math.sqrt(math.pow(c,2)+math.pow(a,2))==b):
			print("triangulo rectangulo")
			return
		print("triangulo escaleno")
	else:
		print("No es un triangulo")	
triangulo(33,21,39.11521443121589)
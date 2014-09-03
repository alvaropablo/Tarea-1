def cerrito(a):
	for x in range(1,a+1):
		imp=""
		for i in range(1,x+1):
			imp=imp+str(x)
		print(imp)
	for x in reversed(range(1,a)):
		imp=""
		for i in range(1,x+1):
			imp=imp+str(x)
		print(imp)
cerrito(5)
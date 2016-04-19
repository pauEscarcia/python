#ejercicio
def RNA():
	ArrLetras=['A','T','C','G']
	cont=0
	cadena=""
	Arrtotal=[]

	for i in ArrLetras:
		for j in ArrLetras:
			for k in ArrLetras:
				for l in ArrLetras:
					cadena= i+j+k+l
					if len(set(cadena))==3:
						cont+=1
						print(cadena)
	print cont	


RNA()


				


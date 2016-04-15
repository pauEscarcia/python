def intercambiar(a,b):
	a1=b
	b1=a
	return a1,b1

def primo(num):
    if num < 2: 
       return False
    for i in range(2, num): 
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    

def mcd(a,b):
	if a<b:	
		a,b=intercambiar(a,b)
	n=a
	d=b
	r= n-(d * (n/d))
	while r!=0:
		n=d
		d=r
		r= n -(d*(n/d))
		print d


def mcdprimo(a,b):
	cont=0
	if a<b:
		a,b=intercambiar(a,b)
	n=a
	d=b
	r= n-(d * (n/d))
	while r!=0:
		n=d
		d=r
		r= n -(d*(n/d))
		print n
		if primo(d)==True:
			cont += 1  
    	return d,cont        
            
numero,contador=mcdprimo(1547,560)
print "Hay", contador, "numero(s) primo(s)"  
print "Es el numero(s): ", numero 	

#otra forma de sacar mcd es con modulo (:
def gcd(a,b):
	if a<b:
		intercambiar (a,b)
	cont = 0
	while b!=0:
		cont += 1        
		r= a %b 
		a=b
		b=r
		print a 
			

def intercambiar(a,b):
	a=b
	b=a

def mcd(a,b):
	if a<b:
		intercambiar(a,b)
	n=a
	d=b
	r= n-(d * (n/d))
	while r!=0:
		n=d
		d=r
		r= n -(d*(n/d))
		print d

mcd(560,1547)

#otra forma de sacarlos (:
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
			
#gcd(1547,560)

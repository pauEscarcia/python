#algoritmo extendido 
def intercambiar(a,b):
	a=b
	b=a
def egcd(a, b):
	x=0
	y=1
	u=1
	v=1
	if a<b:
		intercambiar(a,b)
	while a != 0:
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
		print a
	return b, x, y


egcd(1547,560)
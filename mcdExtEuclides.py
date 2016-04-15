#algoritmo extendido 
def intercambiar(a,b):
	a=b
	b=a
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
        print a 
    return b, x, y


egcd(1547,560)
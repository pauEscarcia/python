#modular inverse 101 mod 1999, 

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
	return b, x, y

def modinv(a, b):
    gcd, x, y = egcd(a, b)
    if gcd != 1:
        return None  # inverso modular no existe
    else: 	
        return x % b

print "Inverso multiplicativo de 101 mod 1999:",modinv(101,1999)
print "Inverso multiplicativo de 1999 mod 101:",modinv(1999,101)

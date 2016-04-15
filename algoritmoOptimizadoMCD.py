def MCDB (a,p):
    u = a
    v = p 
    x1 = 1
    x2 = 0
    while u != 1 and v != 1:
    	while (u % 2) == 0:
    		u = u/2
    		if (x1 % 2) == 0:
    			x1 = x1/2
    		else:
    			x1 = (x1+p)/2
    	while v % 2 == 0:
    		v = v/2
    		if (x2 % 2) == 0:
    			x2 = x2/2
    		else:
    			x2 = (x2+p)/2
    	if u >= v:
    		u = u - v 
    		x1 = x1 - x2
    	else:
    		v = v - u 
    		x2 = x2 - x1
    if u == 1:
    	return x1 % p
    else:
    	return x2 % p

print MCDB (5,101)

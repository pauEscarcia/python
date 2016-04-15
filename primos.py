#numeros primos menores a 1000
def primo(num):
    if num < 2: 
       return False
    for i in range(2, num):  
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    


def primos(num1, num2):  
    cont = 0
    for i in range(num1, num2):
        if primo(i) == True: 
            cont += 1           
            print i                
  
    print ""  
    print "Del", num1, "al",num2
    print "Hay", cont, "numeros primos" 
        
print primos(2,1000)

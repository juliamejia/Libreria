
#Libreria computacion cuantica
#Julia Mejia
#CNYT


import math

#1. suma de numeros complejos 
def sumaComp (a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real,img)

#2. multiplicacion de numeros complejos
def multiComp(a,b):
    real = (a[0]*b[0]) - (a[1]*b[1])
    img = (a[0]*b[1]) + (a[1]*b[0])
    return (real,img)

#3. resta de numeros complejos 
def restaComp (a,b):
    real = a[0]-b[0]
    img = a[1]-b[1]
    return (real,img)


#4. division de numeros complejos 
def divisionComp(a,b):
    numerador1 = a[0] * b[0] + a[1] * b[1]
    denominador1 = b[0]**2 + b[1]**2
    numerador2 = a[1] * b[0] - a[0] * b[1]
    divisor1 = numerador1 / denominador1
    divisor1 = round(divisor1, 2)
    divisor2 = numerador2 / denominador1
    divisor2 = round(divisor2, 2)
    return(divisor1,divisor2)

#5. modulo de numeros complejos
def moduloComp (complejo):
    raiz = math.sqrt(complejo[0]**2 + complejo[1]**2)
    raiz = round(raiz, 2)
    return (raiz)

#6. conjugado de un numero complejo 
def conjugadoComp(complejo):
    return complejo[0] , complejo[1]*-1


#7. conversion de complejo a polar 
def polarComp(complejo):
    r = math.sqrt(complejo[0]**2 + complejo[1]**2)
    r = round(r, 2)
    angulo = math.atan2(complejo[1],complejo[0])
    angulo = round(angulo, 2)
    return (r,angulo)

#8. fase de un numero complejo 
def faseComp(complejo):
    angulo = math.atan2(complejo[1],complejo[0])
    angulo = round(angulo, 2)
    return (angulo)

#------------------------------ SEGUNDA PARTE-----------------------------------
#9. suma de vectores
def sumVectores(a,b):
    matriz =[]
    m = len(a)
    for i in range (m):
        sum1 = sumaComp(a[i],b[i])
        matriz = matriz + [sum1]
    return matriz


#10. inverso aditivo de un numero complejo
def inversoVector(c):
    inversa = []
    a = (-1,0)
    for i in range (len(c)):
        mult1 = multiComp(c[i],a)
        inversa = inversa + [mult1]
        return inversa

#11. multiplicacion de un escalar por una matriz
def multiEscalar (a,b):
    matriz = []
    i =0
    for i in range (len(a)):
        multiplicacion = multiComp((a[i]),(b))
        matriz = matriz + [multiplicacion]
    return matriz

#12. adicion de matrices complejas

#13. inversa de una matriz compleja

#14. multiplicacion de un escalar por una amtriz compleja 


#15. transpuesta de una matriz
def transpuestaMatriz(a):
    n,m = len(y),len(y[0])
    i = 0
    j = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = y[j][i]
    return c

#16. conjugada de una matriz
def conjugadaMatriz ():
    n,m = len(z),len(z[0])
    i = 0
    j = 0
    c = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = conjugadaComp(z[i][j])
    return c

#17. adjunta de una matriz
def adjuntaMatriz(matriz):
    adjunta = conjugadaMatriz(transpuestaMatriz(matriz))
    return matriz

#18. producto de dos matrices (de tamaños compatibles)

#19. calcular la aacion de una matriz sobre un vector

#20. producto interno de dos vectores
#21. norma de un vector
#22. distancia entre dos vectores
#23. revisar si una matriz es unitaria
#24. revisar si una matris es hermitiana
#25. producto tensor de dos matrices 

    


    



def main():
    a = (2,13)
    b = (34,56)
    print(sumaComp(a,b))
    print(restaComp(a,b))
    print(multiComp(a,b))
    print (divisionComp(a,b))
    print(moduloComp(b))
    print(conjugadoComp(b))
    print (polarComp(b))
    print(faseComp(b))
    vector1 = [(5,6),(4,2)]
    vector2 = [(3,4),(4,6)]
    print (sumVectores(vector1,vector2))
    print (inversoVector(vector2))    
    
    

main()
    

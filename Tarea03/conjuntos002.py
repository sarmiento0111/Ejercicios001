
#DIFERENCIA ENTRE 2 CONJUNTOS
numeros1={12,1,3,4,7,8,11,9,0}
numeros2={12,7,3,5,8,0,2,4}
print('NUMEROS1: ',numeros1)
print('cantidad de elementos del conjunto de NUMEROS1: ',len(numeros1))

print()

print('NUMEROS2: ',numeros2)
print('cantidad de elementos del conjunto de NUMEROS2: ',len(numeros2))

print('\n******************DIFRENCIA DE 2 CONJUNTOS******************\n')

diferencia1=numeros1.difference(numeros2)
print('elementos de la diferencia1\n DIFERENCIA1= ',diferencia1)
print('cantidad de elementos del conjunto de NUMEROS2: ',len(diferencia1))

print()

diferencia2=numeros2.difference(numeros1)
print('elementos de la diferencia2\n DIFERENCIA2= ',diferencia2)
print('cantidad de elementos del conjunto de NUMEROS2: ',len(diferencia2))
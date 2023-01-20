conjuntoA={'perro','gato','pez','hamster','marmota','cebra','elefante'}
conjuntoB={'gato','leon','hamster','jirafa','conejo','elefante'}
conjuntoC={'hamster','leon','elefante','gato','ardilla','canguro'}

print('CONJUNTO_A: ',conjuntoA)
print('cantidad de elementos del conjuntoA: ',len(conjuntoA))

print()

print('CONJUNTO_B: ',conjuntoB)
print('cantidad de elementos del conjuntoB: ',len(conjuntoB))

print()

print('CONJUNTO_C: \n',conjuntoC)
print('cantidad de elementos del conjuntoC: ',len(conjuntoC))

print()
# UNION
print('**************UNION DE 3 CONJUNTOS****************\n')
union=conjuntoA|conjuntoB|conjuntoC
#union1=conjuntoA.union(conjuntoB).union(conjuntoC)
print('La union de los 3 conjuntos es: \n UNION= ',union)
print(' cantidad de elementos de la union es: ',len(union))

print()



# INTERSECCION
print('**************INTERSECCION DE 3 CONJUNTOS****************\n')
interseccion=conjuntoA&conjuntoB&conjuntoC
#intersec=conjuntoA.intersection(conjuntoB).intersection(conjuntoC)
print('La interseccion de los 3 conjuntos es: \n INTERSECION= ',interseccion)
print(' cantidad de elementos de la interseccion es: ',len(interseccion))

print()
intersec=conjuntoA.intersection(conjuntoB).intersection(conjuntoC)

# DIFERENCIA
print('**************DIFERENCIA DE 3 CONJUNTOS****************\n')
diferencia1=conjuntoA - conjuntoB - conjuntoC
diferencia2=conjuntoB - conjuntoA - conjuntoC
diferencia3=conjuntoC - conjuntoB - conjuntoA
print('La direncia de conjuntos entre conjuntoA - conjuntoB - conjuntoC es: \n DIFERENCIA1= ',diferencia1)
print(' cantidad de elementos de la diferencia1 es: ',len(diferencia1))
print('\nLa direncia de conjuntos entre conjuntoB - conjuntoA - conjuntoC es: \n DIFRENCIA2= ',diferencia2)
print(' cantidad de elementos de la diferencia2 es: ',len(diferencia2))
print('\nLa direncia de conjuntos entre conjuntoC - conjuntoB - conjuntoA es: \n DIFERENCIA3= ',diferencia3)
print(' cantidad de elementos de la diferencia3 es: ',len(diferencia3))
# 
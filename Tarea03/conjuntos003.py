
# DIFRENCIA SIMETRIA ENTRE 3 CONJUNTOS
conjuntoA={'perro','gato','marmota','cebra','elefante','rinoceronte'}
conjuntoB={'gato','leon','hamster','jirafa','guacamayo'}
conjuntoC={'hamster','leon','elefante','gato','ardilla','perico'}

print('CONJUNTO_A: ',conjuntoA)
print('cantidad de elementos del conjuntoA: ',len(conjuntoA))

print()

print('CONJUNTO_B: ',conjuntoB)
print('cantidad de elementos del conjuntoB: ',len(conjuntoB))

print()

print('CONJUNTO_C: \n',conjuntoC)
print('cantidad de elementos del conjuntoC: ',len(conjuntoC))

print('\n******************DIFRENCIA SIMETRIA******************\n')
dif_semetrica=conjuntoA.symmetric_difference(conjuntoB).symmetric_difference(conjuntoC)
print('La difrencia simetrica de 3 conjuntos es: \n dif_simetrica= ',dif_semetrica)
print(' cantidad de elementos de la dif_simetrica es: ',len(dif_semetrica))

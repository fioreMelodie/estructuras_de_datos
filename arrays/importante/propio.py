#Suma
lista = [1,2,3,4,5]
print(f'La suma de {lista} es igual a: {sum(lista)}')

# Acceder al índice 4
print(f'El índice 4 es: {lista[4]}')
print(f'El último elemento es: {lista[-1]}')

#insert
lista.insert(3,8)
print(lista)

#Remove
lista.remove(8)
print(lista)

#pop
lista.pop(1)
print(lista)

#del
del lista[2]
print(lista)


#sublista
sublista = lista [0:2]
print(sublista)

#nombres
nombres = ['Karla','Juan','Laura']
for n in nombres:
    print(n)
    
#Lista heterogenea
lista_heterogenea = [100,True, 'Sofía']
for elemento in lista_heterogenea:
     print(elemento)
     
#Ejercicio propio
print()
piramide = [1,2,3,4,5,6,7,8,9]

for n in piramide:
    piramide.pop(-1)
    print(piramide)
sub_primaide = piramide[0:]
    
#Función recursiva de a elevado a la x

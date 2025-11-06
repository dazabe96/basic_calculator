# Metodos listas

# Creando una lista con list()
lista = list([29,33,True])

# Devuelve la cantidad de elementos de la lista
cantidad_de_elementos = len(lista)

# Agregando un elemento a la lista (se agrega al final)

# Con append
lista.append(65)

# Con insert() se agrega un elementoa a la lista en un indice especifico
lista.insert(2,"Toma tu insert")

# Con extend() Se agregan varios elementos (osea una lista) a la lista
lista.extend([False,2025])

#Con pop() eliminamos un elemento de la lista, Si ponemos (-1) se borra el ultimo elemento, (-2) el penultimo..
lista.pop(0)

# Con remove() Removemos un elemento por su valor
lista.remove("Toma tu insert")

# Con clear() se eliminan todos los elementos de la lista
#lista.clear()

# Con sort() ordenamos la lista de forma ascendente a descendente (no puede llevar cadenas de texto)
lista.sort() # si usamoe sort(reverse=True) lo invierte

# Con reverse() Se invierten los parametros en una lista
lista.reverse()

# Con Index verificamos si un elemento se encuentra en la lista por posicion
elemento_encontrado = lista.index(65)

print(elemento_encontrado)
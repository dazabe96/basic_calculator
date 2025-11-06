# Metodo Diccionario

diccionario = {
    "nombre" : "Danilo",
    "apellido" : "Zapata",
    "edad" : 29
}

# Con keys() vemos las claves del diccionario (tambien sirve para iterar)
claves = diccionario.keys() #devuelve un objeto dict_item

# Con get() Nos da el valor al que es igual
valor_del_diccionario = diccionario.get("nombre")

# Con clear, se elimina todo lo que haya en el diccionario
# diccionario.clear()

# Con pop podemos borrar un elemento del diccionario
diccionario.pop("nombre")

# obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
# Bucles

# Iterar listas

animales = ["gato","perro","loro","cocodrilo",]
numeros = [2,5,8,9]

# recoriendo la lista animales
for animal in animales:
    print(animal)

# Recorriendo la lista y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# Recorriendo ambas listas en una misma funcion, deben tener el mismo tamaño y se ejecutan al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numero}")
    
# para numero con la funcion range()
for Num in range(5,20):
    print(Num)
    
    
# Forma correcta de recorrer una lista con enumerate
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice}, y el valor es: {valor} ")

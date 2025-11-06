# otros ejemplos

frutas = ["manzana","pera","ciruela","banano","granada","fresa"]
cadena = "hola Danilo"
numeros = (2,3,4,5)

# Usando "continue" saltamos el elemento dentro del bucle
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"me voy a comer la fruta {fruta}")
    
    
# Usando "break" detenemos el bucle cuando llegue al elemento especificado
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"me voy a comer la fruta {fruta}")
    
    
# Recorrer una cadena de texto
for caracter in cadena:
    print(caracter)
    

# for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
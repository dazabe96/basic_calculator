# Ejercicio 1.2

frase = input( "Dime una frase y te calculo cuanto te tardarias si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras, y te tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras / 2 * 0.7} segundos")
if cantidad_de_palabras > 120:
    print("Para por favor, tampoco te pedi un discurso")
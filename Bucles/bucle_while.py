# con while() se va a ejecutar el programa de manera infinita, si no se le da una instruccion clara se va a ejecutar por siempre y puede freeziar el programa

contador = 0

while contador < 10:
    print(contador)
    contador+= 1
    
print("el while llego a su fin")
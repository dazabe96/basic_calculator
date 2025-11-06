# Creando funcion simple

#def saludar():
#    print("Hola Danilo, como vas?")

# Para ejecutar solo se pone el parametro
#saludar()
# y al correr el programa se muestra el mensaje

# Crear una funcion que tenga parametros

def saludar(nombre,sexo):
    sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "Pana"
    else:
        adjetivo = "marica"
        
    print(f"Hola {nombre}, {adjetivo} como estas?")

saludar("Daniela","mujer")

# Condicionales if y else, se usan para condicionar que se ejecute una variable en caso de que se cupla o en caso de que no, se ejecute otra variable

#if = True:
    # se ejecuta la variable

#if = False:
    # No se ejecuta la variable

edad = 14
diferencia_de_edad = 18 - edad
if edad >= 18:
    print("Puedes pasar, bienvenido")
elif edad == 17:
    print(f"Paila, te falta {diferencia_de_edad} año para entrar")
else:
    print(f"Paila, te faltan {diferencia_de_edad} años para entrar")


contraseña_almacenada = "Contraseñacorrecta++"
contraseña_escrita = "Contraseñacorrecta++"

if contraseña_almacenada == contraseña_escrita:
    print("Iniciando Sesion...")
else:
    print("Contraseña errada, intente de nuevo")
    

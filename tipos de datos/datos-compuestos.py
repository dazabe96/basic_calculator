
# Creando una Lista (se puede modificar) 
Lista = ["Danilo Zapata","Curso python",True,1.68,"Daniela","Flor","Santiago","Alejandra","Omar","Summer","Mafe","Leo","Manu","Titi","Oscar"]
print(Lista[10])

# Creando una Tupla (No se puede modificar)
tuple = ("Danilo Zapata","Curso python",True,1.68)

# Creando un conjunto Set (No se puede llamar a los elementos por su indice, no almacena datos duplicados)

conjunto = {"Danilo Zapata","Curso python",True,1.68,"Danilo Zapata"}

print(conjunto)

# Creando un Diccionario (dict) Estructura = 'Key': "Value" ,

Diccionario = {
    "Nombre": "Danilo Zapata",
    'Curso': "Python",
    'Esta emocionado': True,
    'Altura': 1.65,
    'Dato duplicado': "Python"
}
print(Diccionario["Dato duplicado"])

# Metodos de cadena

cadena1 = "Hola,soy,Danilo"
cadena2 = "Bienvenido mi so"


# Mayuscula = "dato".upper()
mayus = cadena1.upper()

# Minuscula = "dato".lower()
minus = cadena1.lower()

# primera mayuscula = "dato".capitalize()
prime_letra_mayus = cadena1.capitalize()

# Buscamos una cadena en otra cadena = "dato".find() si no hay coincidencias devuelve "-1"
busqueda_find = cadena1.find("Danilo")

# Buscamos una cadena en otra cadena = "dato".index() si no hay coincidencias devulve una excepcion
busqueda_index = cadena1.index("Danilo")

# isnumeric =  "dato".isnumeric() si es un dato numerico nos devuelve true
es_numerico = cadena1.isnumeric()

# isalfanumeric =  "dato".isalpha() si es un dato alfanumerico nos devuelve true
es_alfanumerico = cadena1.isalpha()

# Buscamos coincidencias de una cadena en otra cadena = "dato".count() devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("o")

# contamos cuantos caracteres hay en una cadema = "dato".len() 
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza con = "dato".starstwith() nos devuelve true
empieza_con = cadena1.startswith("Hola")

# Verificamos si una cadena termina con = "dato".endswith() nos devuelve true
termina_con = cadena1.endswith("Danilo")

# reemplaza un pedazo de la cadena dada = "dato".replace("Hola" , "Hello")
nueva_cadena = cadena1.replace(",", " ")

# separar cadena con la cadena que le pasemos = 
cadena_separada = cadena1.split(",")





print(cadena_separada)


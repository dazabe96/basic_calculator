# Conjuntos o sets
conjunto = set(["dato1","dato2"])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1,"dato 3"}

# Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# Veiricar si es un subconjunto con conjunto.issubset() o con menor o igual que (<=)
resultado = conjunto2.issubset(conjunto1)

# Veiricar si es un superconjunto con conjunto.issuperset() o con mayor que (>)
resultado = conjunto1.issuperset(conjunto2)

print(resultado)
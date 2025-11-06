# Condicional del Else - If, (elif) = se usa para darle una segunda condicion a la variable que no es el Else ni es el primer IF

ingreso_mensual = 2000
gasto_mensual = 1500

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("Estas melo en plata en cualquier parte del mundo")
    elif ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    else:
        print("Estas gastando mucho papi, cuidado")

elif ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual > 300:
        print("Estas melo en plata en latinoamerica")
    elif ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    else:
        print("Estas gastando mucho papi, cuidado")
    

else:
    print("Tas vaciao mi so")
    
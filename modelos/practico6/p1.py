import numpy as np
import math


def generar_hasta():
    i = 1
    var_list = list()
    count = 0

    for i in range(30):
        var_list.append(np.random.standard_normal())
        count += 1

    m = media(var_list)
    s = desvio(var_list, m)

    while(s/math.sqrt(count) >= 0.1):
        var_list.append(np.random.standard_normal())
        m = media(var_list)
        s = desvio(var_list, m)
        count += 1

    return count, m, s


def media(lista):
    suma = 0.0

    for i in lista:
        suma += i

    return suma/float(len(lista))


def desvio(lista, media):
    suma = 0.0

    for i in lista:
        suma += (i - media) ** 2

    return suma/float(len(lista))


l, m, s = generar_hasta()
print "Datos generados: ", l
print "Media muestral: ", m
print "Varianza muestral: ", s * s

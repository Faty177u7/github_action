def ordenar(array_l):
    array_l.sort()
    return array_l

def cont_mayores(diccionario):
    count = 0
    for i in diccionario:
        if i.get("edad") < 18:
            pass
        else:
            count = count+1
    print("Ya existen: ",count," personas mayores de edad")
    return count
"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


# Cargar datos
def cargar_datos(archivo):
    with open(archivo, "r") as f:
        datos = [linea.strip().split("\t") for linea in f.readlines()]
    return datos


def pregunta_01():
    datos = cargar_datos("data.csv")
    sumaColumna = 0

    for fila in datos:
        numero = int(fila[1])
        sumaColumna += numero

    return sumaColumna


def pregunta_02():
    datos = cargar_datos("data.csv")
    registroColumna = {}
    for fila in datos:
        registro = fila[0]
        if registro not in registroColumna:
            registroColumna[registro] = 1
        else:
            registroColumna[registro] += 1

    registroOrdenado = sorted(registroColumna.items())

    return registroOrdenado


def pregunta_03():
    datos = cargar_datos("data.csv")
    registroColumna = {}
    for fila in datos:
        registro = fila[0]
        numero = int(fila[1])
        if registro not in registroColumna:
            registroColumna[registro] = numero
        else:
            registroColumna[registro] += numero

    registroOrdenado = sorted(registroColumna.items())

    return registroOrdenado


def pregunta_04():
    datos = cargar_datos("data.csv")
    fechasMeses = {}
    for fila in datos:
        fecha = fila[2]
        mes = fecha.split("-")[1]

        if mes not in fechasMeses:
            fechasMeses[mes] = 1
        else:
            fechasMeses[mes] += 1

    mesesOrdenado = sorted(fechasMeses.items())

    return mesesOrdenado


def pregunta_05():
    datos = cargar_datos("data.csv")
    registro = {}
    for fila in datos:
        letra = fila[0]
        numero = int(fila[1])

        if letra not in registro:
            registro[letra] = {"max": numero, "min": numero}
        else:
            registro[letra]["max"] = max(registro[letra]["max"], numero)
            registro[letra]["min"] = min(registro[letra]["min"], numero)

    resultado = [
        (letra, registro[letra]["max"], registro[letra]["min"])
        for letra in sorted(registro)
    ]
    return resultado


def pregunta_06():
    datos = cargar_datos("data.csv")
    dicResultado = {}

    for fila in datos:
        diccionario = fila[4]
        diccionario = diccionario.split(",")

        for elemento in diccionario:
            elemento = elemento.split(":")
            clave = elemento[0]
            valor = int(elemento[1])

            if clave not in dicResultado:
                dicResultado[clave] = {"min": valor, "max": valor}
            else:
                dicResultado[clave]["min"] = min(dicResultado[clave]["min"], valor)
                dicResultado[clave]["max"] = max(dicResultado[clave]["max"], valor)

        resultado = [
            (clave, dicResultado[clave]["min"], dicResultado[clave]["max"])
            for clave in sorted(dicResultado)
        ]

    return resultado


def pregunta_07():
    datos = cargar_datos("data.csv")
    dicRegistros = {}

    for fila in datos:
        letra = fila[0]
        numero = int(fila[1])
        if numero not in dicRegistros:
            dicRegistros[numero] = [letra]
        else:
            dicRegistros[numero].append(letra)

    resultado = sorted(dicRegistros.items())

    return resultado


def pregunta_08():
    datos = cargar_datos("data.csv")
    dicRegistros = {}

    for fila in datos:
        letra = fila[0]
        numero = int(fila[1])
        if numero not in dicRegistros:
            dicRegistros[numero] = set()
        dicRegistros[numero].add(letra)

    resultado = [
        (numero, sorted(letras)) for numero, letras in sorted(dicRegistros.items())
    ]

    return resultado


def pregunta_09():
    datos = cargar_datos("data.csv")
    dicResultado = {}

    for fila in datos:
        diccionario = fila[4]
        diccionario = diccionario.split(",")

        for elemento in diccionario:
            elemento = elemento.split(":")
            clave = elemento[0]

            if clave not in dicResultado:
                dicResultado[clave] = 1
            else:
                dicResultado[clave] += 1

    resultado = dict(sorted(dicResultado.items()))

    return resultado


def pregunta_10():
    datos = cargar_datos("data.csv")
    listaResultado = []

    for fila in datos:
        letra = fila[0]
        elementosCol4 = len(fila[3].split(","))
        elementosCol5 = len(fila[4].split(","))
        listaResultado.append((letra, elementosCol4, elementosCol5))

    return listaResultado


def pregunta_11():
    datos = cargar_datos("data.csv")
    dicResultado = {}

    for fila in datos:
        numero = int(fila[1])
        letras = fila[3].split(",")
        for letra in letras:
            if letra not in dicResultado:
                dicResultado[letra] = numero
            else:
                dicResultado[letra] += numero

    resultado = dict(sorted(dicResultado.items()))

    return resultado


def pregunta_12():
    datos = cargar_datos("data.csv")
    dicResultado = {}
    for fila in datos:
        sumaValores = 0
        letra = fila[0]
        diccionario = fila[4]
        diccionario = diccionario.split(",")

        for item in diccionario:
            item = item.split(":")
            sumaValores += int(item[1])

        if letra not in dicResultado:
            dicResultado[letra] = sumaValores
        else:
            dicResultado[letra] += sumaValores

        resultado = dict(sorted(dicResultado.items()))

    return resultado

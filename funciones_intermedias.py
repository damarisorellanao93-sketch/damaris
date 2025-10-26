#1. Modificar elementos
matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Elementos modificados
matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

# 2. Iterar a través de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

#Formato del diccionario
def iterarDiccionario(lista):
    for dic in lista:
        for llave, valor in dic.items():
            print(f"{llave} - {valor}")

#Formato 'BONUS'
def iterarDiccionario0(lista):
    for dic in lista:
        resultado = ", ".join([f"{llave} - {valor}" for llave, valor in dic.items()])
        print(resultado)

iterarDiccionario0(cantantes)


#3.Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for i in lista:
        if llave in i:
            print(i[llave])

print("Nombres de los cantantes:")
iterarDiccionario2("nombre", cantantes)

print("Países de los cantantes:")
iterarDiccionario2("pais", cantantes)

#4.Iterar a través de un diccionario con valores de lista
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave, valor in diccionario.items():
        print(f"{len(valor)} {clave.upper()}")
        for e in valor:
            print(e)

imprimirInformacion(costa_rica)

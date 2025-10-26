#1.Básico: imprime todos los números enteros del 0 al 100
print("Ejercicio Básico")
for i in range(101):
    print(i)

#2.Múltiplos de 2: imprime todos los múltiplos de 2 entre 2 y 500
print("Ejercicio de múltiplos de 2")
for i in range(2, 501, 2):
    print(i)

#3.Contando Vanilla Ice, si es divisible por 5, imprime “ice ice" y si es divisible por 10, imprime “baby”
print("Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

#4.Número gigante a la vista, suma los números pares del 0 al 500,000 e imprime la suma total
print("Número gigante a la vista")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("La suma total es:", suma)

#5.Regrésame al 3, e imprime los números positivos desde 2024 hasta 0, en cuenta regresiva de 3 en 3
print("Regrésame al 3")
for i in range(2024, 0, -3):
    print(i)

#6. Contador dinámico, el usuario elige los valores para probar el bucle
print("Contador dinámico")
numero_inicial = int(input("Ingresa el número inicial: "))
numero_final = int(input("Ingresa el número final: "))
multiplo = int(input("Ingresa el número múltiplo: "))

print(f"Números entre {numero_inicial} y {numero_final} que son múltiplos de {multiplo}:")
for i in range(numero_inicial, numero_final + 1):
    if i % multiplo == 0:
        print(i)
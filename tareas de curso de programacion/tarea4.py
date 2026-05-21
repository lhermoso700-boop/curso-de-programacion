#Manipulación Básica de Listas
numeros = []
numeros.append(10)
numeros.append(20)
numeros.append(30)
numeros.append(40)
numeros.append(50)

numeros.pop(2)
print(f"Lista final: {numeros}")
#Creación de un Directorio
libro = {
    "título": "El Psicoanalista",
    "autor": "John Katzenbach",
    "año": 2002
}

autor_libro = libro["autor"]
print("El autor del libro es:", autor_libro)
#Calculo gemetrico
import math

radio = 7.5
area = math.pi * (radio ** 2)

print("El área del círculo es:", round(area, 2))
#juego de adivinaza
import random
numero_secreto = random.randint(1, 10)
intentos_maximos = 3

print("¡He pensado un número del 1 al 10! Tienes 3 intentos para adivinarlo.")

for intento in range(1, intentos_maximos + 1):
    posible_numero = int(input(f"Intento {intento}: Ingresa tu número: "))
    
    if posible_numero == numero_secreto:
        print("¡Excelente! Acertaste el número.")
        break
    else:
        print("Fallaste.")
else:
    print(f"Te quedaste sin intentos. El número era el {numero_secreto}.")
#analizador de numeros
def analizar_numeros(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division_entera = num1 // num2 
    
    return (suma, resta, multiplicacion, division_entera)

resultado_suma, resultado_resta, resultado_mult, resultado_div = analizar_numeros(15, 4)

print("Resultados del análisis:")
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}, Multiplicación: {resultado_mult}, División entera: {resultado_div}")
#filtro de aleatoridad
import random

lista_original = []
pares = []
impares = []

for _ in range(15):
    lista_original.append(random.randint(1, 50))

for num in lista_original:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista completa generada:", lista_original)
print("Números pares:", pares)
print("Números impares:", impares)
#gestor de clasificaciones
estudiantes = {
    "Carlos": [15, 18, 14],
    "María": [20, 19, 18],
    "José": [12, 10, 11]
}
for nombre, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    print(f"Estudiante: {nombre} | Promedio: {round(promedio, 2)}")
#analisis de texto
def analizar_vocabulario(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    en_ambas = conjunto1.intersection(conjunto2)
    
    exclusivas_primera = conjunto1.difference(conjunto2)
    
    print("Palabras en ambas listas:", en_ambas)
    print("Palabras exclusivas de la primera lista:", exclusivas_primera)

palabras_a = ["python", "codigo", "computadora", "logica"]
palabras_b = ["programacion", "logica", "python", "pantalla"]

analizar_vocabulario(palabras_a, palabras_b)
#distancia geometrica
import random
import math

def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

punto_A = (random.randint(0, 10), random.randint(0, 10))
punto_B = (random.randint(0, 10), random.randint(0, 10))

resultado_distancia = calcular_distancia(punto_A, punto_B)

print(f"Punto A: {punto_A}")
print(f"Punto B: {punto_B}")
print(f"La distancia euclidiana entre ellos es: {round(resultado_distancia, 2)}")
#simulador de inventario
inventario = {
    "harina": 20,
    "arroz": 15,
    "pasta": 10
}

print("    SISTEMA DE CONTROL DE INVENTARIO    ")
print("Productos disponibles:", list(inventario.keys()))

while True:
    producto_venta = input("\n¿Qué producto deseas vender? (o escribe 'salir'): ").lower()
    
    if producto_venta == "salir":
        print("Saliendo del sistema de inventario. ¡Hasta luego!")
        break   
    if producto_venta in inventario:
        cantidad = int(input(f"¿Cuántas unidades de {producto_venta} vas a vender?: "))
        if cantidad <= inventario[producto_venta]:
            inventario[producto_venta] -= cantidad 
            print(f"Venta exitosa. Stock restante de {producto_venta}: {inventario[producto_venta]}")
        else:
            print(f"¡Error! No hay suficiente stock. Solo quedan {inventario[producto_venta]} unidades.")
    else:
        print("Ese producto no existe en el inventario actual. Intenta de nuevo.")
print("programa 1")
#conteo basico secuencial
for i in range(1, 16):
    print(i)

print("programa 2")
#conteo regresivo
n = 10
while n >= 0:
    print(n)
    n-=1

print("programa 3")
#sumatoria de rango
suma_total = 0
for i in range(1, 51):
     suma_total += i
print(f"la suma total de los primeros 50 numeros es: {suma_total}")

print("programa 4")
#generador de tabla de multiplicar
numero = int(input("ingrese el numero para ver su tabla: "))
for i in range (1, 11):
    print(f"{numero} x {i} = {numero * i}")
    
print("programa 5")
#interacion de cadenas
palabra = "programacion"
for letra in palabra:
    print(letra)

print("programa 6")
#identificacion de numeros pares
contador = 2
while contador <=30:
    print(contador)
    contador += 2
    
print("programa 7")
#interrupcion de bucle
for i in range (1, 101):
    if i % 13 == 0:
        print(f"¡alto! el numero divisible por 13 es {i}")
        break
    print(i)
    
print("programa 8")
#calculo de factorial
num = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
    
print(f"El factorial de {num} es: {factorial}")

print("programa 9")
#filtro de vocales
frase = input("Escribe una frase: ").lower()
vocales = "aeiou"
cantidad = 0

for letra in frase:
    if letra in vocales:
        cantidad += 1

print(f"Tu frase tiene {cantidad} vocales.")

print("programa 10")
#salto de iteracion
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
    
print("programa 11")
#inversion de cadenas
palabra = input("Ingresa una palabra para invertirla: ")
palabra_invertida = ""

for letra in palabra:
    palabra_invertida = letra + palabra_invertida 

print(f"Al revés se lee: {palabra_invertida}")

print("programa 12")
#Secuencia de Fibonacci
n_terminos = int(input("¿Cuántos términos de Fibonacci quieres ver?: "))
a, b = 0, 1

for _ in range(n_terminos):
    print(a)
    a, b = b, a + b  
    
print("progama 13")
#Bucle Centinela (Adivinanza)
numero_secreto = 42

while True:
    intento = int(input("Adivina el número secreto: "))
    if intento == numero_secreto:
        print("¡Exacto! Adivinaste la respuesta a la vida, el universo y todo lo demás.")
        break
    else:
        print("Sigue intentando...")
        
print("programa 14")
#validacion constante
while True:
    numero = float(input("Por favor, ingresa un número estrictamente positivo: "))
    if numero > 0:
        print(f"¡Gracias! Ingresaste {numero}.")
        break
    print("Error. El número debe ser mayor a cero.")
    
print("programa 15")
#identificador de primos
n = int(input("Ingresa un número para saber si es primo: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} NO es primo. Es divisible por {i}.")
            break
    else:
        # Este else pertenece al for, se ejecuta solo si el bucle no fue interrumpido por un break
        print(f"¡{n} SÍ es un número primo!")
else:
    print(f"{n} NO es primo.")
    
print("programa 16")
#Rango de primos
limite = int(input("¿Hasta qué número quieres buscar primos?: "))

for num in range(2, limite + 1):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
        
print("programa 17")
#patron geometrico
base = int(input("De qué tamaño quieres la base del triángulo: "))

for i in range(1, base + 1):
    fila = ""
    for j in range(i):
        fila += "*"
    print(fila)
    
print("programa 18")
#algoritmo de Euclides
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
original_a, original_b = a, b

while b != 0:
    residuo = a % b
    a = b
    b = residuo

print(f"El MCD de {original_a} y {original_b} es: {a}")

print("programa 19")
#menu interactivo
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Mostrar motivación")
    print("3. Salir del programa")
    
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == '1':
        print("\n¡Hola! Qué bueno verte programando.")
    elif opcion == '2':
        print("\n¡Tú puedes! La constancia es la clave del éxito.")
    elif opcion == '3':
        print("\n¡Hasta la próxima! Cerrando sistema...")
        break
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")
        
print("programa 20")
#analisis de matriz
matriz = [[1, 5, 9],[2, 6, 10],[3, 7, 11]]

suma_total = 0

for fila in matriz:
    for numero in fila:
        suma_total += numero

print(f"La suma de todos los elementos de la matriz es: {suma_total}")
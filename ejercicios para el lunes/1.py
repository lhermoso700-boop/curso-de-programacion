#isentificador de numeros pares
numero = int(input("ingresa un numero entero: "))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")
    
#sumatoria acumulativa
limite = int(input("ingresa el limite: "))
suma_total = 0

for i in range(1, limite + 1):
    suma_total += i

print("la suma acumulativa es:", suma_total)
#filtrado de positivos
numeros = [-5, 3, -1, 10, 0, 8, -2]
positivos = []

for num in numeros:
    if num > 0:
        positivos.append(num)

print("lista de positivos:", positivos)
#contador de vocales
frase = input("ingresa una frase: ")
vocales = "aeiou"
contador = 0

for letra in frase.lower():
    if letra in vocales:
        contador += 1

print("la frase tiene", contador, "vocales")
#adivina el numero
numero_secreto = 7
intento = 0

while intento != numero_secreto:
    intento = int(input("adivina el numero del 1 al 10: "))

print("ganaste, adivinaste el numero.")

#calculadora de promedios
estudiantes = {
    "Carlos": [15, 18, 14],
    "María": [20, 19, 18],
    "José": [12, 10, 11]
}
for nombre, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    print(f"Estudiante: {nombre} | Promedio: {round(promedio, 2)}")
    
#identificador de primos
n = int(input("Ingresa un número para saber si es primo: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} NO es primo. Es divisible por {i}.")
            break
    else:
        print(f"¡{n} SÍ es un número primo!")
else:
    print(f"{n} NO es primo.")
    
#interseccion de datos
lista_a = [1, 2, 3, 4, 5, 2, 3]
lista_b = [3, 4, 5, 6, 7, 5]

set_a = set(lista_a)
set_b = set(lista_b)
comunes = list(set_a & set_b)

print("elementos comunes sin duplicados:", comunes)

#tabla de multiplicar
for i in range(1, 6):
    print("tabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("-" * 15)
    
#clasificacion de edades
personas = [("pedro", 12), ("lucia", 25), ("carlos", 68), ("sofia", 18)]

for nombre, edad in personas:
    if edad < 18:
        clasificacion = "menor"
    elif edad < 65:
        clasificacion = "adulto"
    else:
        clasificacion = "mayor"
    print(nombre, "es", clasificacion)
#simulacion bancaria
class cuentabancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        print("deposito exitoso. nuevo saldo:", self.saldo)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("retiro exitoso. nuevo saldo:", self.saldo)
        else:
            print("fondos insuficientes")

mi_cuenta = cuentabancaria("leonardo", 100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(200)
mi_cuenta.retirar(40)
#desplazamiento de bits
numero = 5
desplazamientos = [1, 2]

for d in desplazamientos:
    resultado = numero << d
    if d == 1:
        print(numero, "multiplicado por 2 es:", resultado)
    else:
        print(numero, "multiplicado por 4 es:", resultado)
#frecuencia de palabras
parrafo = "los kniks no merecian el campionato"
palabras = parrafo.split()
frecuencia = {}

for pal in palabras:
    pal_limpia = pal.lower()
    if pal_limpia in frecuencia:
        frecuencia[pal_limpia] += 1
    else:
        frecuencia[pal_limpia] = 1

print("frecuencia de palabras:", frecuencia)
#susecion de fibonacci
n = 8
fibonacci = []
a, b = 0, 1

while len(fibonacci) < n:
    fibonacci.append(a)
    a, b = b, a + b

print("serie fibonacci:", fibonacci)
#suma de matrices
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

print("matriz resultante de la suma:")
for fila in resultado:
    print(fila)
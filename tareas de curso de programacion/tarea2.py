
print("validacion de fecha")
dia = int(input("ingresa el dia: "))
mes = int(input("ingresa el mes: "))
año = int(input("ingresa el año: "))
if mes in [1,3,5,7,8,10,12] and 1 <= dia <= 31:
    print("fecha valida")
elif mes in [4,6,9,11] and 1 <= dia <= 30:
    print("fecha valida")
elif mes == 2:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        if 1 <= dia <= 29:
            print("fecha valida")
        else:
            print("fecha no valida")
    else:
        if 1 <= dia <= 28:
            print("fecha valida")
        else:
            print("fecha no valida")
else:    print("fecha no valida")  


print("validacion de triangulo")
lado1 = float(input("ingresa el lado 1: "))
lado2 = float(input("ingresa el lado 2: "))
lado3 = float(input("ingresa el lado 3: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 >
    lado2) and (lado2 + lado3 > lado1):
        print("los lados forman un triangulo valido")
        if (lado1**2 + lado2**2 == lado3**2) or (lado1**2 + lado3**2 == lado2**2) or (lado2**2 + lado3**2 == lado1**2):
            print("el triangulo es rectangulo")
        elif (lado1**2 + lado2**2 > lado3**2) and (lado1**2 + lado3**2 > lado2**2) and (lado2**2 + lado3**2 > lado1**2):
            print("el triangulo es acutangulo")
        else:
            print("el triangulo es obtusangulo")
else:    print("los lados no forman un triangulo valido")


print("colision de cajas")
print("ingresa las coordenadas del rectangulo 1")
x1_min = float(input("x min: "))
y1_min = float(input("y min: "))
x1_max = float(input("x max: "))
y1_max = float(input("y max: "))
print("ingresa las coordenadas del rectangulo 2")
x2_min = float(input("x min: "))
y2_min = float(input("y min: "))
x2_max = float(input("x max: "))
y2_max = float(input("y max: "))
if (x1_min < x2_max and x1_max > x2_min and y1_min < y2_max and y1_max > y2_min):
    print("los rectangulos se chocan")
else:
    print("los rectangulos no se chocan")
    

print("reloj con adicion de segundos")
hora = int(input("ingresa la hora (0-23): "))
minutos = int(input("ingresa los minutos (0-59): "))
segundos = int(input("ingresa los segundos (0-59): "))
segundos_a_sumar = int(input("ingresa los segundos a sumar: "))
total_segundos = hora * 3600 + minutos * 60 + segundos + segundos_a_sumar
nueva_hora = (total_segundos // 3600) % 24
nuevos_minutos = (total_segundos % 3600) // 60
nuevos_segundos = total_segundos % 60
print(f"la nueva hora es: {nueva_hora:02d}:{nuevos_minutos:02d}:{nuevos_segundos:02d}")


print("simulador de compuertas logicas")
bool1 = input("ingresa el primer booleano (true/false): ").lower() == "true"
bool2 = input("ingresa el segundo booleano (true/false): ").lower() == "true"
compuerta = input("ingresa la compuerta (XOR, NAND, NOR, XNOR): ").upper()
if compuerta == "XOR":
    resultado = (bool1 and not bool2) or (not bool1 and bool2)
elif compuerta == "NAND":
    resultado = not (bool1 and bool2)
elif compuerta == "NOR":
    resultado = not (bool1 or bool2)
elif compuerta == "XNOR":
    resultado = (bool1 and bool2) or (not bool1 and not bool2)
else:
    resultado = "compuerta no valida"
print(f"el resultado de la compuerta {compuerta} es: {resultado}")


print("clasificacion estricta IPv4")
octeto1 = int(input("ingresa el primer octeto (0-255): "))
octeto2 = int(input("ingresa el segundo octeto (0-255): "))
octeto3 = int(input("ingresa el tercer octeto (0-255): "))
octeto4 = int(input("ingresa el cuarto octeto (0-255): "))
if 0 <= octeto1 <= 255 and 0 <= octeto2 <= 255 and 0 <= octeto3 <= 255 and 0 <= octeto4 <= 255:
    if 0 <= octeto1 <= 127:
        clase = "A"
    elif 128 <= octeto1 <= 191:
        clase = "B"
    elif 192 <= octeto1 <= 223:
        clase = "C"
    elif 224 <= octeto1 <= 239:
        clase = "D"
    else:
        clase = "E"
    print(f"la direccion IP {octeto1}.{octeto2}.{octeto3}.{octeto4} es de clase {clase}")
else:    print("direccion IP no valida")


print("juego de piedra papel tijera lagarto spock")
nombre_J1 = input("ingresa tu nombre J1: ")
nombre_J2 = input("ingresa tu nombre J2: ")
jug1 = input(f"{nombre_J1} elige(piedra,papel,tijera,lagarto,spock): ").lower()
jug2 = input(f"{nombre_J2} elige(piedra,papel,tijera,lagarto,spock): ").lower()
if (jug1 == "piedra" and (jug2 == "tijera" or jug2 == "lagarto")) or (jug1 == "papel" and (jug2 == "piedra" or jug2 == "spock")) or (jug1 == "tijera" and (jug2 == "papel" or jug2 == "lagarto")) or (jug1 == "lagarto" and (jug2 == "spock" or jug2 == "papel")) or (jug1 == "spock" and (jug2 == "tijera" or jug2 == "piedra")):
    print(f"{nombre_J1} has ganado")
elif (jug2 == "piedra" and (jug1 == "tijera" or jug1 == "lagarto")) or (jug2 == "papel" and (jug1 == "piedra" or jug1 == "spock")) or (jug2 == "tijera" and (jug1 == "papel" or jug1 == "lagarto")) or (jug2 == "lagarto" and (jug1 == "spock" or jug1 == "papel")) or (jug2 == "spock" and (jug1 == "tijera" or jug1 == "piedra")):
    print(f"{nombre_J2} has ganado")
else:
    print("empate")
    

print("impuesto marginal de multiples tramos")
ingreso = float(input("ingresa tu ingreso anual: "))
if ingreso <= 10000:
    impuesto = 0
elif ingreso <= 30000:
    impuesto = (ingreso - 10000) * 0.15
elif ingreso <= 60000:
    impuesto = (20000 * 0.15) + (ingreso - 30000) * 0.25
else:
    impuesto = (20000 * 0.15) + (30000 * 0.25) + (ingreso - 60000) * 0.35
print(f"el impuesto a pagar es: ${impuesto:.2f}")


print("compatibilidad sanguinea")
grupo_donante = input("ingresa el grupo sanguineo del donante (A, B, AB, O): ").upper()
factor_donante = input("ingresa el factor Rh del donante (positivo/negativo): ").lower()
grupo_receptor = input("ingresa el grupo sanguineo del receptor (A, B, AB, O): ").upper()
factor_receptor = input("ingresa el factor Rh del receptor (positivo/negativo): ").lower()
compatible = False
if factor_donante == "negativo":
    compatible = True
elif factor_donante == "positivo" and factor_receptor == "positivo":
    compatible = True
print(f"la transfusion es {'segura' if compatible else 'no segura'}")


print("decodificador de permisos en linux (chmod)")
permiso = int(input("ingresa un numero del 0 al 7: "))
if 0 <= permiso <= 7:
    permisos = []
    if permiso & 4:
        permisos.append("lectura")
    if permiso & 2:
        permisos.append("escritura")
    if permiso & 1:
        permisos.append("ejecucion")
    print(f"el numero {permiso} otorga los siguientes permisos: {', '.join(permisos) if permisos else 'ninguno'}")
else:
    print("numero no valido")


print("evaluador de credito (scoring)")
ingreso = float(input("ingresa tu ingreso mensual: "))
deudas = float(input("ingresa el total de tus deudas: "))
edad = int(input("ingresa tu edad: "))
morosidad = int(input("ingresa el numero de veces que has sido moroso: "))
puntos = 100
if ingreso > 5000:
    puntos += 20
elif ingreso > 2000:
    puntos += 10
else:
    puntos -= 10
if deudas < ingreso * 0.3:
    puntos += 10
else:
    puntos -= 10
if 25 <= edad <= 65:
    puntos += 10
else:
    puntos -= 10
if morosidad == 0:
    puntos += 20
elif morosidad == 1:
    puntos += 10
else:
    puntos -= 10
print(f"tu puntaje de credito es: {puntos}")


print("signo zodiacal exacto")
dia = int(input("ingresa el dia: "))
mes = int(input("ingresa el mes: "))
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"  
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
else:    signo = "fecha no valida"
print(f"tu signo zodiacal es: {signo}")


print("calculadora logistica")
zona = input("ingresa la zona de destino (nacional, internacional): ").lower()
peso = float(input("ingresa el peso del paquete en kg: "))
volumen = float(input("ingresa el volumen del paquete en m3: "))
costo_base = 100 if zona == "nacional" else 200
costo_peso = peso * 50
costo_volumen = volumen * 100
costo_total = costo_base + costo_peso + costo_volumen
premium = input("¿tienes membresia premium? (si/no): ").lower()
if premium == "si":
    costo_total *= 0.9
print(f"el costo total del envio es: ${costo_total:.2f}")


print("evaluador de tic-tac-toe")
tablero = [input(f"ingresa la casilla {i+1} (X/O/ ): ").upper() for i in range(9)]
if (tablero[0] == tablero[1] == tablero[2] == "X") or (tablero[3] == tablero[4] == tablero[5] == "X") or (tablero[6] == tablero[7] == tablero[8] == "X") or (tablero[0] == tablero[3] == tablero[6] == "X") or (tablero[1] == tablero[4] == tablero[7] == "X") or (tablero[2] == tablero[5] == tablero[8] == "X") or (tablero[0] == tablero[4] == tablero[8] == "X") or (tablero[2] == tablero[4] == tablero[6] == "X"):
    print("¡X ha ganado!")
else:
    print("X no ha ganado.")
    

print("identificador de cuadrantes")
x = float(input("ingresa la coordenada x: "))
y = float(input("ingresa la coordenada y: "))
if x > 0 and y > 0:
    print("el punto está en el cuadrante 1")
elif x < 0 and y > 0:
    print("el punto está en el cuadrante 2")
elif x < 0 and y < 0:
    print("el punto está en el cuadrante 3")
elif x > 0 and y < 0:
    print("el punto está en el cuadrante 4")
elif x == 0 and y == 0:
    print("el punto está en el origen")
elif x == 0:
    print("el punto está sobre el eje Y")
elif y == 0:
    print("el punto está sobre el eje X")
else:
    print("coordenadas no válidas")
    print("fin del programa")
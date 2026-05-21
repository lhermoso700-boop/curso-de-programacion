print("programa 1")
edad = int(input("ingrese su año de nacimiento: "))
if edad >= 1946 and edad <= 1964:
    print("su generacin es baby boomer")
elif edad >= 1965 and edad <= 1980:
    print("su gerenacion es gen X")
elif edad >= 1981 and edad <=1996:
    print("su generacion es millenial")
elif edad >= 1997 and edad <= 2012:
    print("su generacion es gen Z")
else:
    print("no entras en el rango")
    
print("programa 2")
contraseña = input("Ingresa la contraseña: ")
longitud = len(contraseña)
if 8<= longitud <20:
    print("contraseña valida")
else:
    print("contraseña no valida debe contener 8 caracteres")  
    
print("programa 3")
numero = int(input("ingrese su numero: "))
if numero % 5 == 0:
    print(f"{numero} es mltiplo de 5")
else:
    print(f"{numero} no es multiplo de 5")
    
print("programa 4")

vehiculo = input("ingrese el tipo de vehiculo (automovil,motocicleta,camion): ").lower()
es_hora_pico = input("es hora pico(si/no): ").lower()

precios={"automovil":5, "motocicleta":2, "camion":10}
if vehiculo in precios:
    costo_base = precios[vehiculo]
    if es_hora_pico == "si":
        print(f"total a pagar={costo_base*1.20}$")
    elif es_hora_pico == "no":
        print(f"total a pagar={costo_base}$")
else:
    print("vehiculo no valido")
    
print("programa 5")
print("hola bienvenido")

edad = int(input("ingresa tu edad: "))
saldo = int(input("ingrese su saldo bancario: "))
prestamo = input("desea pedir un prestamo(si/no): ").lower()
if prestamo == "si" and saldo > 3000 and edad >=25:
        print("prestamo aprobado")
elif prestamo == "si" and saldo >= 1500 and saldo <= 3000 and edad >=25:
        print("prestamo aprobado con aval")
elif edad <25 or saldo <1500 and prestamo == "si":
        print("prestamo negado")
else:
    print("gracias por informar")
    
print("juego de piedra papel o tijeras")
nombre_J1 = input("ingresa tu nombre J1: ")
nombre_J2 = input("ingresa tu nombre J2: ")

jug1 = input(f"{nombre_J1} elige(piedra,papel,tijera): ").lower()
jug2 = input(f"{nombre_J2} elige(piedra,papel,tijera): ").lower()
if (jug1 == "piedra" and jug2 == "tijera") or (jug1 == "tijera" and jug2 == "papel") or (jug1 == "papel" and jug2 == "piedra"):
    print(f"{nombre_J1} has ganado")
elif (jug2 == "piedra" and jug2 == "tijera") or (jug2 == "tijera" and jug1 == "papel") or (jug2 == "papel" and jug1 == "piedra"):
    print(f"{nombre_J2} has ganado")
elif jug1 == jug2:
    print(f"{nombre_J1} y {nombre_J2} han empatado")
else:
    print("no valido")

print("programa 7")

categoria = input("ingresa categoria (electrinica/ropa): ").lower()
cantidad = int(input("ingrese la cantidad: "))
precio_unitario = float(input("ingrese el precio unitario: "))
descuento = 0.0
if categoria == "electronica" and cantidad >=3:
    descuento = 0.10
elif categoria == "ropa" and cantidad >=5:
    descuento = 0.15
subtotal = cantidad * precio_unitario
monto_descuento = subtotal * descuento
total_final = subtotal - monto_descuento
print(f"subtotal ${subtotal}")
print(f"descuento aplicado: {descuento*100}% (-${monto_descuento})")
print(f"total a pagar: ${total_final}")
print("FIN")
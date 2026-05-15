pin_correcto = "1234"
intentos = 3
saldo = 1000
bloqueado = False
while intentos > 0:
    ingreso = input(f"Introduce tu PIN ({intentos} intentos restantes): ")
    if ingreso == pin_correcto:
        print("PIN Correcto. Bienvenido al Cajero Pro.")
        break
    else:
        intentos -= 1
        print("PIN incorrecto.")
        if intentos == 0:
            bloqueado = True
if not bloqueado:
    opcion = ""
    while opcion != "4":
        print("    MENÚ CAJERO   ")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(f"Tu saldo actual es: ${saldo}")
        
        elif opcion == "2":
            deposito = float(input("Monto a depositar: "))
            saldo += deposito
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")

        elif opcion == "3":
            monto = int(input("Monto a retirar (Múltiplos de 10): "))
            
            if monto > saldo:
                print("Fondos insuficientes.")
            elif monto % 10 != 0:
                print("Error: El monto debe ser múltiplo de 10.")
            elif monto <= 0:
                print("Monto inválido.")
            else:
                saldo -= monto
                print(f" Retirando ${monto}...")
                
                b100 = monto // 100
                monto %= 100
                
                b50 = monto // 50
                monto %= 50
                
                b20 = monto // 20
                monto %= 20
                
                b10 = monto // 10
                
                print(f"Entregando: {b100} de $100, {b50} de $50, {b20} de $20 y {b10} de $10.")
                print(f"Nuevo saldo: ${saldo}")

        elif opcion == "4":
            print("Gracias por usar nuestro sistema. ¡Hasta pronto!")
        else:
            print("Opción no válida.")
else:
    print("Cuenta bloqueada por seguridad. Contacta con tu banco.")   
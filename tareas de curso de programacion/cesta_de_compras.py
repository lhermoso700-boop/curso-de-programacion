cesta = []

def mostrar_menu():
    print(" SIMULADOR DE CESTA DE COMPRA ")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar contenido de la cesta")
    print("3. Eliminar un elemento")
    print("4. Calcular el total de la compra")
    print("5. Renunciar (Salir)")

def agregar_elemento():
    print("\n--- Añadir Artículo ---")
    nombre = input("¿Qué artículo deseas agregar?: ").strip().capitalize()
    
    if not nombre:
        print(" El nombre del artículo no puede estar vacío.")
        return

    entrada_precio = input(f"¿Cuánto cuesta '{nombre}'? ($): ").strip()
    
    entrada_precio = entrada_precio.replace(",", ".")

    try:
        precio = float(entrada_precio)
        if precio < 0:
            print(" El precio no puede ser negativo.")
            return
        
        articulo = {"nombre": nombre, "precio": precio}
        cesta.append(articulo)
        print(f" ¡'{nombre}' ha sido agregado a la cesta con éxito por ${precio:.2f}!")
    except ValueError:
        print(" Error: Por favor, introduce un número válido (ejemplo: 15.50 o 15,50).")

def mostrar_cesta():
    print("\n---  Tu Cesta de Compra ---")
    if len(cesta) == 0:
        print("Tu cesta está vacía. ¡Empieza a comprar! ")
        return
    for indice, articulo in enumerate(cesta, start=1):
        print(f"{indice}. {articulo['nombre']} - ${articulo['precio']:.2f}")

def eliminar_elemento():
    print("\n---  Eliminar Artículo ---")
    if len(cesta) == 0:
        print("No hay nada que eliminar, tu cesta está vacía. ")
        return
    
    mostrar_cesta()
    try:
        opcion = int(input("\nIntroduce el número del artículo que deseas eliminar: "))
        if 1 <= opcion <= len(cesta):
            eliminado = cesta.pop(opcion - 1)
            print(f" Se ha eliminado '{eliminado['nombre']}' de la cesta.")
        else:
            print(" Ese número de artículo no existe en tu cesta.")
    except ValueError:
        print(" Error: Por favor, introduce un número entero válido.")

def calcular_total():
    print("\n---  Total de la Compra ---")
    if len(cesta) == 0:
        print("El total es $0.00 (Tu cesta está vacía).")
        return
    
    total = sum(articulo['precio'] for articulo in cesta)
    mostrar_cesta()
    print("-"*30)
    print(f" Total acumulado: ${total:.2f}")
    print("="*30)

def ejecutar_simulador():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_elemento()
        elif opcion == "2":
            mostrar_cesta()
        elif opcion == "3":
            eliminar_elemento()
        elif opcion == "4":
            calcular_total()
        elif opcion == "5":
            print("\n ¡Gracias por usar el simulador! Feliz viernes. \n")
            break
        else:
            print(" Opción no válida. Por favor, elige un número del 1 al 5.")

if __name__ == "__main__":
    ejecutar_simulador()
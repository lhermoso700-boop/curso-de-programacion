print("   🐳BIENVENIDO A UNA GRAN AVENTURA EN EL OCEANO🐳   ")
personaje = input("selecciona a tu personaje para sobrevivir (ORCA, TIBURON): ").strip().lower()
if personaje == "orca":
    print("🐳⚫️⚪️buena eleccion la habilidad de tu personaje es: ")
    print("Embestida de Alta Velocidad: Capacidad de golpear con la cabeza o la cola para aturdir a la presa (los golpes a la cabeza hacen mas daño). ")
    opcion1 = input("estas en medio del oceano con mucha hambre a la distancia vez a una FOCA, ¿que decides cazarla? (si/no): ").strip().lower()
    if personaje == "orca" and opcion1 == "si":
        print("perfecto ahora vas camino a cazar a la foca pero te encuentras con un megalodon que te esta cazando a ti")
        opcion1_1 = input("¿Que decides hacer? (luchar con el megalodon, seguir el camino hacia la foca): ").strip().lower()
        if personaje == "orca" and opcion1 == "si" and opcion1_1 == "luchar con el megalodon":
            print("ya estas luchando con el megalodon pero te queda un ultimo ataque")
            opcion1_1_1 = input("¿donde decides pegarle? (cabeza, cola): ").strip().lower()
            if personaje == "orca" and opcion1 == "si" and opcion1_1 == "luchar con el megalodon" and opcion1_1_1 == "cabeza":
                print(" 🏆has ganado ya puedes seguir con tu camino campeon🏆 ")
            elif personaje == "orca" and opcion1 == "si" and opcion1_1 == "luchar con el megalodon" and opcion1_1_1 == "cola":
                print(" 💀has perdido, el golpe a la cabeza hace mas daño.💀 ")
            else:
                print("respuesta no valida")
        elif personaje == "orca" and opcion1 == "si" and opcion1_1 == "seguir el camino hacia la foca":
            print(" 💀has perdido el megalodon te ha alcanzado y matado💀 ")
        else:
            print("respuesta no valida")
    elif personaje == "orca" and opcion1 == "no":
        print(" 💀has perdido si no buscas tu comida te mueres de hambre💀")
    else:
        print(" respuesta no valida ")
elif personaje == "tiburon":
    print("🦈perfecto que buena eleccion la habilidad de tu personaje es: ")
    print("mordisco preciso: capacidad ara infligir heridas graves a presas o rivales")
    opcion2 = input("Nadas cerca de un arrecife y detectas un grupo de ATUNES. ¿Decides atacar? (si/no): ").strip().lower()
    if opcion2 == "si":
        print("¡Ataque exitoso! Estás dándote un banquete, pero de repente el agua se vuelve turbia.")
        print("¡Es una RED DE PESCA que está subiendo hacia la superficie y estás atrapado!")
        opcion2_1 = input("¿Que decides hacer? (romper la red / nadar hacia abajo con fuerza): ").strip().lower()
        if opcion2 == "si" and opcion2_1 == "romper la red":
            print("Usas tu 'Mordisco Preciso' contra las cuerdas de la red ")
            opcion2_1_1 = input("¿Dónde muerdes para escapar? (nudo principal / malla lateral): ").strip().lower()
            if opcion2 == "si" and opcion2_1 == "romper la red" and opcion2_1_1 == "nudo principal":
                print("🏆 ¡Increíble! Has cortado la base de la red y escapas hacia las profundidades. ¡Eres libre! 🏆")
            elif opcion2 == "si" and opcion2_1 == "romper la red" and opcion2_1_1 == "malla lateral":
                print("💀 La malla es demasiado elástica y tus dientes se enredan más. Los pescadores te han subido al barco. 💀")
            else:
                print("respuesta no valida.")
        elif opcion2 == "si" and opcion2_1 == "nadar hacia abajo con fuerza":
            print("💀 La red es demasiado grande y pesada; intentar arrastrarla te agotó los músculos. Has muerto por cansancio. 💀")
        else:
            print("respuesta no valida.")
    elif opcion2 == "no":
        print("💀 Un tiburon que no caza pierde su lugar en la cadena alimenticia. Has muerto de hambre. 💀")
    else:
        print("respuesta no valida")
else:
    print("respuesta no valida")
import math
import random


def sample_analysis(n):
    numbers = [random.randint(1, 100) for _ in range(n)]
    unique_numbers = set(numbers)
    maximum = max(unique_numbers) if unique_numbers else 0
    root = math.sqrt(maximum)
    return {
        'lista': numbers,
        'conjunto': unique_numbers,
        'raiz_maxima': root,
    }


def lottery_system(user_numbers=None):
    winners = []
    while len(winners) < 3:
        candidate = random.randint(1, 20)
        if candidate not in winners:
            winners.append(candidate)
    winners_tuple = tuple(winners)

    if user_numbers is None:
        user_numbers = [random.randint(1, 20) for _ in range(3)]

    matches = set(winners_tuple).intersection(user_numbers)
    match_count = len(matches)

    if match_count == 3:
        prize = 1000 * match_count
    elif 1 <= match_count <= 2:
        prize = 200 * match_count // 1
    else:
        prize = 0

    return {
        'ganadores': winners_tuple,
        'usuario': user_numbers,
        'aciertos': matches,
        'premio': prize,
    }


def dynamic_price_processor():
    products = ('Camisa', 'Pantalón', 'Zapatos', 'Sombrero', 'Bufanda')
    prices = {}
    final_prices = set()

    for product in products:
        price = random.randint(20, 80)
        if price > 50:
            price += price * 0.15
        price = math.ceil(price)
        prices[product] = price
        final_prices.add(price)

    return {
        'precios_finales': prices,
        'precios_unicos': final_prices,
    }


def particle_geometry():
    radios = [random.randint(1, 10) for _ in range(10)]
    particle_data = {}
    unique_areas = set()

    for index, radio in enumerate(radios):
        area = math.pi * (radio ** 2)
        particle_data[index] = (radio, area)
        unique_areas.add(area)

    return {
        'radios': radios,
        'particulas': particle_data,
        'areas_unicas': unique_areas,
    }


def numeric_cipher(numbers):
    key = random.randint(1, 9)
    mapping = {}
    encrypted_values = set()

    for number in numbers:
        if number % 2 == 0:
            ciphered = number + key
        else:
            ciphered = number - key
        mapping[number] = ciphered
        encrypted_values.add(ciphered)

    return key, mapping, encrypted_values


def weather_station_analysis():
    stations = {
        'Norte': tuple(random.randint(-5, 35) for _ in range(5)),
        'Sur': tuple(random.randint(-5, 35) for _ in range(5)),
        'Este': tuple(random.randint(-5, 35) for _ in range(5)),
        'Oeste': tuple(random.randint(-5, 35) for _ in range(5)),
    }
    averages = {}
    anomalies = set()

    for station, temps in stations.items():
        total = 0
        for temp in temps:
            total += temp
            if temp < 0 or temp > 30:
                anomalies.add((station, temp))
        average = total / len(temps)
        averages[station] = math.floor(average)

    return {
        'estaciones': stations,
        'promedios': averages,
        'anomalías': anomalies,
    }


def rpg_battle_engine():
    player = {'HP': 120, 'Defensa': 8}
    enemy = {'HP': 100, 'Defensa': 6}
    historial = []

    while player['HP'] > 0 and enemy['HP'] > 0:
        base_damage = random.randint(12, 25)
        mitigation = math.ceil(enemy['Defensa'] / 2)
        damage = max(base_damage - mitigation, 1)
        enemy['HP'] -= damage
        historial.append(('Jugador', damage))

        if enemy['HP'] <= 0:
            break

        base_damage = random.randint(10, 22)
        mitigation = math.ceil(player['Defensa'] / 2)
        damage = max(base_damage - mitigation, 1)
        player['HP'] -= damage
        historial.append(('Enemigo', damage))

    ganador = 'Jugador' if enemy['HP'] <= 0 else 'Enemigo'
    return ganador, tuple(historial)


def network_pattern_validator():
    ips = [
        tuple(random.randint(0, 255) for _ in range(4))
        for _ in range(5)
    ]
    prohibidos = {0, 127, 255}
    clasificacion = {}

    for ip in ips:
        bloqueo = any(octeto in prohibidos for octeto in ip)
        peso = sum(ip)
        valor = math.log(peso + 1) if peso >= 0 else 0
        if bloqueo:
            clasificacion[ip] = 'No válido'
        elif valor > 5:
            clasificacion[ip] = 'Alto'
        else:
            clasificacion[ip] = 'Bajo'

    return {
        'ips': ips,
        'clasificación': clasificacion,
    }


def navigation_system():
    origen = (0, 0)
    destinos = [
        (random.randint(-10, 10), random.randint(-10, 10))
        for _ in range(5)
    ]
    distancias = set()
    mapa = {}

    for destino in destinos:
        distancia = math.hypot(destino[0] - origen[0], destino[1] - origen[1])
        mapa[destino] = distancia
        distancias.add(distancia)

    return {
        'origen': origen,
        'destinos': destinos,
        'distancias_unicas': distancias,
        'mapa': mapa,
    }


def inventory_optimizer():
    zonas = {
        'Zona A': 100,
        'Zona B': 80,
        'Zona C': 120,
    }
    carga_actual = {zona: 0 for zona in zonas}
    desbordadas = set()

    for entrega in range(1, 11):
        volumen = random.randint(10, 60)
        zona = list(zonas)[entrega % len(zonas)]
        carga_actual[zona] += volumen
        sobrante = math.fmod(carga_actual[zona], zonas[zona])
        if carga_actual[zona] > zonas[zona]:
            desbordadas.add(zona)
        cargar = (zona, volumen, sobrante)

    return carga_actual, desbordadas


if __name__ == '__main__':
    random.seed(42)

    print('1) Análisis de Muestras Aleatorias:')
    print(sample_analysis(10))
    print('\n2) Sistema de Lotería Matemático:')
    print(lottery_system([3, 7, 12]))
    print('\n3) Procesador de Precios Dinámico:')
    print(dynamic_price_processor())
    print('\n4) Geometría de Partículas Aleatorias:')
    print(particle_geometry())
    print('\n5) Cifrado Numérico por Desplazamiento:')
    key, mapping, unique = numeric_cipher([10, 15, 20, 25, 30])
    print({'clave': key, 'mapeo': mapping, 'valores_unicos': unique})
    print('\n6) Análisis de Estaciones Meteorológicas:')
    print(weather_station_analysis())
    print('\n7) Motor de Batalla RPG Básico:')
    print(rpg_battle_engine())
    print('\n8) Validador de Patrones de Red:')
    print(network_pattern_validator())
    print('\n9) Sistema de Navegación Cartográfica:')
    print(navigation_system())
    print('\n10) Optimizador de Inventario Logístico:')
    print(inventory_optimizer())

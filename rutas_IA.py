import heapq
import random

# ---------------------------
# BASE DE CONOCIMIENTO (GRAFO BIDIRECCIONAL)
# ---------------------------
grafo = {
    "A": {"B": (5, 10), "C": (2, 4)},
    "B": {"A": (5, 10), "D": (1, 3)},
    "C": {"A": (2, 4), "D": (2, 5), "E": (4, 8)},
    "D": {"B": (1, 3), "C": (2, 5), "F": (3, 6)},
    "E": {"C": (4, 8), "F": (1, 2)},
    "F": {"D": (3, 6), "E": (1, 2)}
}

# ---------------------------
# DIJKSTRA (RUTA ÓPTIMA)
# ---------------------------
def dijkstra(grafo, inicio, fin):
    cola = [(0, 0, inicio, [inicio])]
    visitados = set()

    while cola:
        tiempo, distancia, nodo, ruta = heapq.heappop(cola)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == fin:
            return tiempo, distancia, ruta

        for vecino, (t, d) in grafo[nodo].items():
            if vecino not in visitados:
                heapq.heappush(cola, (tiempo + t, distancia + d, vecino, ruta + [vecino]))

    return float("inf"), float("inf"), []

# ---------------------------
# RUTA ALTERNATIVA (SIN CICLOS)
# ---------------------------
def ruta_simple(grafo, inicio, fin):
    actual = inicio
    ruta = [actual]
    visitados = set([actual])
    tiempo_total = 0
    distancia_total = 0

    while actual != fin:
        vecinos = list(grafo[actual].keys())
        opciones = [v for v in vecinos if v not in visitados]

        if not opciones:
            break

        siguiente = random.choice(opciones)
        t, d = grafo[actual][siguiente]

        tiempo_total += t
        distancia_total += d
        ruta.append(siguiente)

        visitados.add(siguiente)
        actual = siguiente

    return tiempo_total, distancia_total, ruta

# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
print("=== SISTEMA INTELIGENTE DE RUTAS ===")
print("Estaciones disponibles:", list(grafo.keys()))

inicio = input("Ingrese punto de inicio: ").upper()
fin = input("Ingrese punto de destino: ").upper()

# Validación
if inicio not in grafo or fin not in grafo:
    print("Error: estación no válida")
else:
    t_opt, d_opt, ruta_opt = dijkstra(grafo, inicio, fin)
    t_alt, d_alt, ruta_alt = ruta_simple(grafo, inicio, fin)

    nombres = ["Ruta Express", "Ruta Óptima", "Ruta Inteligente", "Ruta Rápida"]
    nombre_ruta = random.choice(nombres)

    print("\n", nombre_ruta)
print("Ruta:", " -> ".join(ruta_opt))
print("Tiempo total:", t_opt, "min")
print("Distancia total:", d_opt, "km")

print("\nRuta alternativa (no optimizada):")
print("Ruta:", " -> ".join(ruta_alt))
print("Tiempo:", t_alt, "min")
print("Distancia:", d_alt, "km")

print("\nComparacion:")
print("Tiempo ahorrado:", t_alt - t_opt, "min")
print("Distancia ahorrada:", d_alt - d_opt, "km")
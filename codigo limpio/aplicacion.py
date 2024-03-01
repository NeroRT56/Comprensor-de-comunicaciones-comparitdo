import unittest
import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
        

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(frecuencias):
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencias.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        nodo_izquierda = heapq.heappop(cola_prioridad)
        nodo_derecha = heapq.heappop(cola_prioridad)

        nodo_combinado = NodoHuffman(None, nodo_izquierda.frecuencia + nodo_derecha.frecuencia)
        nodo_combinado.izquierda = nodo_izquierda
        nodo_combinado.derecha = nodo_derecha

        heapq.heappush(cola_prioridad, nodo_combinado)

    return cola_prioridad[0]

def generar_codigos_huffman(arbol, codigo_actual="", diccionario_codigos=None):
    if diccionario_codigos is None:
        diccionario_codigos = {}

    if arbol.caracter is not None:
        diccionario_codigos[arbol.caracter] = codigo_actual
    if arbol.izquierda is not None:
        generar_codigos_huffman(arbol.izquierda, codigo_actual + "0", diccionario_codigos)
    if arbol.derecha is not None:
        generar_codigos_huffman(arbol.derecha, codigo_actual + "1", diccionario_codigos)

    return diccionario_codigos

def comprimir_datos(datos):
    frecuencias = defaultdict(int)
    for caracter in datos:
        frecuencias[caracter] += 1

    arbol_huffman = construir_arbol_huffman(frecuencias)
    diccionario_codigos = generar_codigos_huffman(arbol_huffman)

    # Modificar la salida de la función para incluir información sobre el árbol
    datos_comprimidos = f"{arbol_huffman}|{'|'.join(diccionario_codigos[caracter] for caracter in datos)}"

    return datos_comprimidos

def descomprimir_datos(datos_comprimidos):
    # Extraer el árbol Huffman y los datos comprimidos
    arbol_huffman_str, datos_comprimidos_str = datos_comprimidos.split('|', 1)
    arbol_huffman = eval(arbol_huffman_str)  # Usar eval para convertir la cadena a objeto

    datos_descomprimidos = []
    nodo_actual = arbol_huffman

    for bit in datos_comprimidos_str:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha

        if nodo_actual.caracter is not None:
            datos_descomprimidos.append(nodo_actual.caracter)
            nodo_actual = arbol_huffman

    return ''.join(datos_descomprimidos)

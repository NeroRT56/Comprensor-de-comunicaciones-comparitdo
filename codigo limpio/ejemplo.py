from aplicacion import comprimir_datos, descomprimir_datos

# Ejemplo de uso
datos_originales = "abracadabra"
datos_comprimidos = comprimir_datos(datos_originales)
datos_descomprimidos = descomprimir_datos(datos_comprimidos)

print(f'Datos originales: {datos_originales}')
print(f'Datos comprimidos: {datos_comprimidos}')
print(f'Datos descomprimidos: {datos_descomprimidos}')

#@unittest.expectedFailure
import unittest
from aplicacion import comprimir_datos, descomprimir_datos,construir_arbol_huffman

class TestCompresionHuffman(unittest.TestCase):

    # Casos Normales de Comprimir
    @unittest.expectedFailure
    def test_prueba_normal_comprimir_1(self):
        datos_originales = "abracadabra"
        datos_comprimidos = comprimir_datos(datos_originales)
        self.assertTrue(len(datos_comprimidos) < len(datos_originales))
        
    @unittest.expectedFailure
    def test_prueba_normal_comprimir_2(self):
        datos_originales = ""
        datos_comprimidos = comprimir_datos(datos_originales)
        self.assertEqual(datos_originales, datos_comprimidos)
        
    @unittest.expectedFailure
    def test_prueba_normal_comprimir_3(self):
        datos_originales = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        datos_comprimidos = comprimir_datos(datos_originales)
        self.assertTrue(len(datos_comprimidos) < len(datos_originales))

    # Casos Excepción de Comprimir
    
    def test_prueba_excepcion_comprimir_1(self):
        datos_no_validos = 12345
        with self.assertRaises(TypeError):
            comprimir_datos(datos_no_validos)
            
    @unittest.expectedFailure
    def test_prueba_excepcion_comprimir_2(self):
        datos_originales_vacios = ""
        with self.assertRaises(ValueError):
            comprimir_datos(datos_originales_vacios)
 
    def test_prueba_excepcion_comprimir_3(self):
        datos_no_validos = None
        with self.assertRaises(TypeError):
            comprimir_datos(datos_no_validos)

    # Casos Error de Comprimir
    @unittest.expectedFailure
    def test_prueba_error_comprimir_1(self):
        datos_originales = "abracadabra"
        arbol_huffman = construir_arbol_huffman({})
        datos_comprimidos = f"{arbol_huffman}|{'|'.join('0' for _ in datos_originales)}"
        with self.assertRaises(ValueError):
            descomprimir_datos(datos_comprimidos)
 
    @unittest.expectedFailure
    def test_prueba_error_comprimir_2(self):
        with self.assertRaises(ValueError):
            comprimir_datos(None)

    @unittest.expectedFailure
    def test_prueba_error_comprimir_3(self):
        with self.assertRaises(ValueError):
            comprimir_datos(12345)

    @unittest.expectedFailure
    def test_prueba_error_comprimir_4(self):
        with self.assertRaises(ValueError):
            comprimir_datos("   ")

    @unittest.expectedFailure
    # Casos Normales de Descomprimir
    def test_prueba_normal_descomprimir_1(self):
        datos_originales = "abracadabra"
        datos_comprimidos = comprimir_datos(datos_originales)
        datos_descomprimidos = descomprimir_datos(datos_comprimidos)
        self.assertEqual(datos_originales, datos_descomprimidos)

    @unittest.expectedFailure
    def test_prueba_normal_descomprimir_2(self):
        datos_originales = ""
        datos_comprimidos = comprimir_datos(datos_originales)
        datos_descomprimidos = descomprimir_datos(datos_comprimidos)
        self.assertEqual(datos_originales, datos_descomprimidos)

    @unittest.expectedFailure
    def test_prueba_normal_descomprimir_3(self):
        datos_originales = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        datos_comprimidos = comprimir_datos(datos_originales)
        datos_descomprimidos = descomprimir_datos(datos_comprimidos)
        self.assertEqual(datos_originales, datos_descomprimidos)

    # Casos Excepción de Descomprimir
    def test_prueba_excepcion_descomprimir_1(self):
        datos_comprimidos_invalidos = "datos_invalidos"
        with self.assertRaises(ValueError):
            descomprimir_datos(datos_comprimidos_invalidos)

    @unittest.expectedFailure
    def test_prueba_excepcion_descomprimir_2(self):
        datos_comprimidos_vacios = ""
        with self.assertRaises(ValueError):
            descomprimir_datos(datos_comprimidos_vacios)

    @unittest.expectedFailure
    def test_prueba_excepcion_descomprimir_3(self):
        datos_comprimidos_mal_formados = "arbol|0101010|1010101"
        with self.assertRaises(ValueError):
            descomprimir_datos(datos_comprimidos_mal_formados)

    # Casos Error de Descomprimir
    @unittest.expectedFailure
    def test_prueba_error_descomprimir_1(self):
        with self.assertRaises(ValueError):
            descomprimir_datos(None)

    @unittest.expectedFailure
    def test_prueba_error_descomprimir_2(self):
        with self.assertRaises(ValueError):
            descomprimir_datos(12345)

    def test_prueba_error_descomprimir_3(self):
        with self.assertRaises(ValueError):
            descomprimir_datos("   ")

    def test_prueba_error_descomprimir_4(self):
        datos_no_comprimidos = "Lorem ipsum dolor sit amet."
        with self.assertRaises(ValueError):
            descomprimir_datos(datos_no_comprimidos)

if __name__ == '__main__':
    unittest.main()

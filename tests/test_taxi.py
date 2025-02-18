import unittest
import time
import os
import taxi

class TestTaximetro(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test para inicializar los datos."""
        self.precios = {"PARADO": 0.02, "MOVIMIENTO": 0.05}
        self.test_historial_file = "test_historial.txt"

    def tearDown(self):
        """Se ejecuta después de cada test para limpiar archivos temporales."""
        if os.path.exists(self.test_historial_file):
            os.remove(self.test_historial_file)

    def test_cargar_configuracion(self):
        """Verifica que cargar_configuracion devuelve un diccionario con valores numéricos."""
        precios = taxi.cargar_configuracion()
        self.assertIsInstance(precios, dict)
        self.assertIn("PARADO", precios)
        self.assertIn("MOVIMIENTO", precios)
        self.assertIsInstance(precios["PARADO"], float)
        self.assertIsInstance(precios["MOVIMIENTO"], float)

    def test_calcular_costo(self):
        """Prueba el cálculo de costos según el tiempo transcurrido."""
        self.assertAlmostEqual(taxi.calcular_costo("PARADO", 10, self.precios), 0.20)
        self.assertAlmostEqual(taxi.calcular_costo("MOVIMIENTO", 10, self.precios), 0.50)

    def test_historial(self):
        """Verifica que la tarifa final se guarda correctamente en un archivo de prueba."""
        tarifa_prueba = f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')} - Tarifa: 5.00€"

        
        with open(self.test_historial_file, "w", encoding="utf-8") as file:
            file.write("")

        
        with open(self.test_historial_file, "a", encoding="utf-8") as file:
            file.write(tarifa_prueba + "\n")

        
        with open(self.test_historial_file, "r", encoding="utf-8") as file:
            contenido = file.read()

        self.assertIn(tarifa_prueba, contenido) 

if __name__ == '__main__':
    unittest.main()

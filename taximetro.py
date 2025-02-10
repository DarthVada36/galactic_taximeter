from config import PRECIOS
import time
from datetime import datetime
import logging
import sys

class Taximetro:
    def __init__(self):
        self.precios = PRECIOS
        self.total = 0
        self.estado_actual = "PARADO"
        self.tiempo_inicio = None
        logging.basicConfig(filename="logs.txt", level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")
        sys.stdout.reconfigure(encoding='utf-8')
    
    def cargar_configuracion(self):
        precios = {"PARADO": 0.02, "MOVIMIENTO": 0.05}
        try:
            with open("config.txt", "r") as file:
                for line in file:
                    clave, valor = line.strip().split("=")
                    precios[clave] = float(valor)
        except FileNotFoundError:
            print("Archivo de configuración no encontrado. Se usarán valores predeterminados.")
        return precios
    
    def log_event(self, message, level="info", save_to_historial=False):
        if level == "info":
            logging.info(message)
        elif level == "warning":
            logging.warning(message)
        
        if save_to_historial:
            with open("historial.txt", "a", encoding="utf-8") as file:
                file.write(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    
    def guardar_historial(self):
        self.log_event(f"Tarifa: {self.total:.2f}€", save_to_historial=True)
    
    def calcular_costo(self, estado, tiempo_transcurrido):
        return tiempo_transcurrido * self.precios[estado.upper()]
    
    def iniciar_viaje(self):
        if self.estado_actual == "MOVIMIENTO":
            return {"error": "El taxi ya está en movimiento."}
        
        self.total = 0
        self.tarifa = 0
        self.estado_actual = "MOVIMIENTO"
        self.tiempo_inicio = time.time()
        self.log_event("Trayecto iniciado.")
        return {"mensaje": "Trayecto iniciado.", "estado": self.estado_actual}
    

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in ["PARADO", "MOVIMIENTO"]:
            return {"error": "Estado no válido. Debe ser 'PARADO' o 'MOVIMIENTO'."}

        if self.estado_actual == nuevo_estado:
            return {"error": "El taxi ya está en ese estado."}

        # Calcular el tiempo transcurrido y acumular la tarifa
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
        self.total += self.calcular_costo(self.estado_actual, tiempo_transcurrido)

        # Cambiar el estado y resetear el tiempo de inicio
        self.estado_actual = nuevo_estado
        self.tiempo_inicio = time.time()
        self.log_event(f"Estado cambiado a {self.estado_actual}.")
        return {"mensaje": f"Estado cambiado a {self.estado_actual}", "tarifa_acumulada": round(self.total, 2)}

    def obtener_tarifa_acumulada(self):
        if self.tiempo_inicio:  # Asegurar que hay un viaje en curso
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
            return round(self.total + self.calcular_costo(self.estado_actual, tiempo_transcurrido), 2)
        
        return round(self.total, 2)


    def finalizar_viaje(self):
        # Calcular la tarifa final si el taxi está en movimiento
        if self.estado_actual == "MOVIMIENTO":
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
            self.total += self.calcular_costo(self.estado_actual, tiempo_transcurrido)

        # Guardar la tarifa final en el archivo historial
        timestamp = time.time()
        fecha = datetime.fromtimestamp(timestamp)
        fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S')

        with open('historial.txt', 'a', encoding="utf-8") as file:
            file.write(f"Fecha: {fecha_formateada} - Tarifa: {self.total:.2f}€\n")

        # Guardar la tarifa total antes de reiniciar
        tarifa_total = round(self.total, 2)

        # Cambiar el estado a "FINALIZADO" en lugar de resetear todo
        self.estado_actual = "FINALIZADO"
        self.tiempo_inicio = None  # Para que no siga acumulando tiempo

        self.log_event(f"Viaje finalizado. Tarifa total: {tarifa_total}€")

        return {
            "mensaje": f"Viaje finalizado. Tarifa total: {tarifa_total}€",
            "estado": self.estado_actual, 
            "tarifa_total": tarifa_total
        }



    # def calcular_tarifa(self, inputs=None):
    #     print("\n✅ Trayecto iniciado. Usa 'parado', 'movimiento' o 'fin' para controlar el estado del taxi.")
    #     index = 0
    #     while True:
    #         if inputs:
    #             if index >= len(inputs):
    #                 break
    #             entrada = inputs[index]
    #             index += 1
    #         else:
    #             entrada = input("Estado del taxi (parado/movimiento/fin): ").strip().lower()
            
    #         tiempo_actual = time.time()
    #         tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
            
    #         if entrada == "fin":
    #             self.total += self.calcular_costo(self.estado_actual, tiempo_transcurrido)
    #             self.guardar_historial()
    #             self.log_event(f"Trayecto finalizado. Tarifa total: {self.total:.2f}€")
    #             print(f"🚖 Viaje finalizado. Tarifa total: {self.total:.2f}€\n")
    #             print("👋 ¡Gracias por Viajar con nosotros!")
    #             return  # Volver al menú principal
            
    #         if entrada in ["parado", "movimiento"]:
    #             self.total += self.calcular_costo(self.estado_actual, tiempo_transcurrido)
    #             self.estado_actual = entrada.upper()
    #             self.tiempo_inicio = time.time()
    #             self.log_event(f"Estado cambiado a: {self.estado_actual}")
    #         else:
    #             print("❌ Estado inválido. Ingresa 'parado' o 'movimiento'.")
    #             self.log_event(f"Entrada inválida: {entrada}", level="warning")
            
    #         print(f"💰 Tarifa acumulada: {self.total:.2f}€")
    
    # def mostrar_bienvenida(self):
    #     print("\n🚖 Bienvenido al Taxímetro Digital")
    #     print("Este programa calcula la tarifa en función del tiempo del trayecto.")
    #     print("Tarifas:")
    #     print(f"  - Taxi detenido: {self.precios['PARADO']:.2f}€ por segundo")
    #     print(f"  - Taxi en movimiento: {self.precios['MOVIMIENTO']:.2f}€ por segundo")
    #     print("Puedes finalizar el viaje en cualquier momento ingresando 'fin'.\n")
    
    # def iniciar(self, inputs=None):
    #     while True:
    #         self.log_event("Programa iniciado.")
    #         self.mostrar_bienvenida()
    #         index = 0
    #         while True:
    #             if inputs:
    #                 if index >= len(inputs):
    #                     return
    #                 opcion = inputs[index]
    #                 index += 1
    #             else:
    #                 opcion = input("¿Quieres iniciar un trayecto? (s/n): ").strip().lower()
                
    #             if opcion == "s":
    #                 self.log_event("Iniciando un nuevo trayecto.")
    #                 self.total = 0  # Reiniciar tarifa
    #                 self.estado_actual = "PARADO"
    #                 self.tiempo_inicio = time.time()
    #                 self.calcular_tarifa()
    #                 break  # Volver al inicio del loop para preguntar otra vez
    #             elif opcion == "n":
    #                 self.log_event("Saliendo del programa.")
    #                 print("👋 Gracias por usar el taxímetro. ¡Hasta luego!")
    #                 return
    #             else:
    #                 print("❌ Opción inválida. Ingresa 's' para iniciar o 'n' para salir.")
    #                 self.log_event(f"Entrada inválida: {opcion}", level="warning")

if __name__ == "__main__":
    taximetro = Taximetro()
    taximetro.iniciar()

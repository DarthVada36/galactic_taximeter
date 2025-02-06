import time  # Para medir el tiempo transcurrido
import logging

# Configuración de registro
logging.basicConfig(filename="logs.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    )

def guardar_historial(total):

    with open("historial.txt", "a") as file:
        file.write(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')} - Tarifa: {total:.2f}€\n")


def cargar_configuracion():
    precios = {"PARADO": 0.02, "MOVIMIENTO": 0.05}

    try:
        with open("config.txt", "r") as file:
            for line in file:
                clave, valor = line.strip().split("=")
                precios[clave] = float(valor)
    except FileNotFoundError:
        print("Archivo de configuración no encontrado. Se utilizarán los valores predeterminados.")

    return precios

def mostrar_bienvenida(precios):
    """Muestra el mensaje de bienvenida e instrucciones con los precios actuales."""
    print("\n🚖 Bienvenido al Taxímetro Digital")
    print("Este programa calcula la tarifa en función del tiempo del trayecto.")
    print("Tarifas:")
    print(f"  - Taxi detenido: {precios['PARADO']:.2f}€ por segundo")
    print(f"  - Taxi en movimiento: {precios['MOVIMIENTO']:.2f}€ por segundo")
    print("Puedes finalizar el viaje en cualquier momento ingresando 'fin'.\n")


def log_event(message, level="info", save_to_historial=False):
    """Registra eventos en logs.txt y opcionalmente en historial.txt."""
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)

    # Solo guardar tarifas finales en historial.txt
    if save_to_historial:
        with open("historial.txt", "a", encoding="utf-8") as file:
            file.write(f"Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')} - Tarifa: {message.split(': ')[-1]}\n")


def calcular_costo(estado, tiempo_transcurrido, precios):
    """Calcula el costo en función del estado y el tiempo transcurrido."""
    return tiempo_transcurrido * precios[estado.upper()]


def calcular_tarifa(precios):
    """Inicia y calcula el costo del trayecto."""   
    total = 0
    estado_actual = "PARADO"
    tiempo_inicio = time.time()  # Guarda el tiempo de inicio 
    print("\n✅ Trayecto iniciado. Escribe 'parado' o 'movimiento' según el estado del taxi.")
    
    
    while True:
        entrada = input("Estado del taxi (parado/movimiento/fin): ").strip().lower()
        tiempo_actual = time.time() # Obtiene el tiempo actual
        tiempo_transcurrido = tiempo_actual - tiempo_inicio  # Calcula tiempo desde el último estado

        
        if entrada == "fin":
            total += calcular_costo(estado_actual, tiempo_transcurrido, precios)
            log_event(f"Viaje Finalizado Tarifa: {total:.2f}€", save_to_historial=True)
            break

        if entrada in ["parado", "movimiento"]:
            # Calculamos el costo antes de cambiar de estado
            total += calcular_costo(estado_actual, tiempo_transcurrido, precios)
            estado_actual = entrada.upper()
            tiempo_inicio = time.time()  # Reiniciar el contador de tiempo
            log_event(f"Estado cambiado a: {estado_actual}")
        else:
            print("❌ Estado inválido. Ingresa 'parado' o 'movimiento'.")
            log_event(f"Entrada inválida: {entrada}", level="warning")
            
        print(f"💰 Tarifa acumulada: {total:.2f}€")

    print(f"\n🔚 Trayecto finalizado. Tarifa total: {total:.2f}€\n")

def main():
    """Función principal del programa."""
    log_event("Programa iniciado.")
    precios = cargar_configuracion()
    mostrar_bienvenida(precios)
    
    while True:
        opcion = input("¿Quieres iniciar un trayecto? (s/n): ").strip().lower()
        
        if opcion == "s":
            log_event("Iniciando un nuevo trayecto.")
            calcular_tarifa(precios)
        elif opcion == "n":
            log_event("Saliendo del programa.")
            print("👋 Gracias por usar el taxímetro. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Ingresa 's' para iniciar o 'n' para salir.")
            log_event(f"Entrada inválida: {opcion}", level="warning")

# Ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    main()

import time  # Para medir el tiempo transcurrido

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

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida e instrucciones."""
    precios = cargar_configuracion()
    if precios:
        print("\n Bienvenido al Taxímetro Digital")
        print("Este programa calcula la tarifa en función del tiempo del trayecto.")
        print("Tarifas:")
        print(f"  - Taxi detenido: {precios['PARADO']:.2f}€ por segundo")
        print(f"  - Taxi en movimiento: {precios['MOVIMIENTO']:.2f}€ por segundo")
        print("Puedes finalizar el viaje en cualquier momento ingresando 'fin'.\n")
    else:
        print("No se pudieron cargar las configuraciones.")

def calcular_tarifa():
    """Inicia y calcula el costo del trayecto."""   
    total = 0
    estado_actual = None
    tiempo_inicio = time.time()  # Guarda el tiempo de inicio 
    print("\n✅ Trayecto iniciado. Escribe 'parado' o 'movimiento' según el estado del taxi.")
    
    
    while True:
        entrada = input("Estado del taxi (parado/movimiento/fin): ").strip().lower()
        tiempo_actual = time.time() # Obtiene el tiempo actual
        tiempo_transcurrido = tiempo_actual - tiempo_inicio  # Calcula tiempo desde el último estado
        
        precios = cargar_configuracion()

        if estado_actual == "parado":
            total += tiempo_transcurrido * precios["PARADO"]  # 2 céntimos por segundo
        elif estado_actual == "movimiento":
            total += tiempo_transcurrido * precios["MOVIMIENTO"]  # 5 céntimos por segundo
        
        if entrada == "fin":
            break

        if entrada in ["parado", "movimiento"]:
            estado_actual = entrada
            tiempo_inicio = time.time()
        else:
            print("❌ Estado inválido. Ingresa 'parado' o 'movimiento'.")
            
        print(f"💰 Tarifa acumulada: {total:.2f}€")

    print(f"\n🔚 Trayecto finalizado. Tarifa total: {total:.2f}€\n")

def main():
    """Función principal del programa."""
    mostrar_bienvenida()
    
    while True:
        opcion = input("¿Quieres iniciar un trayecto? (s/n): ").strip().lower()
        
        if opcion == "s":
            calcular_tarifa()
        elif opcion == "n":
            print("👋 Gracias por usar el taxímetro. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Ingresa 's' para iniciar o 'n' para salir.")

# Ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    main()

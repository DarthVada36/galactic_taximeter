import time  # Para medir el tiempo transcurrido

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida e instrucciones."""
    print("\n Bienvenido al Taxímetro Digital s")
    print("Este programa calcula la tarifa en función del tiempo del trayecto.")
    print("Tarifas:")
    print("  - Taxi detenido: 0.02€ por segundo")
    print("  - Taxi en movimiento: 0.05€ por segundo")
    print("Puedes finalizar el viaje en cualquier momento ingresando 'fin'.\n")

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
        

        if estado_actual == "parado":
            total += tiempo_transcurrido * 0.02  # 2 céntimos por segundo
        elif estado_actual == "movimiento":
            total += tiempo_transcurrido * 0.05  # 5 céntimos por segundo
        
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

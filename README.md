# 🚕 Taxímetro Digital - Cyberpunk 2077

## 📌 Descripción
Este es un **taxímetro digital** inspirado en el universo de **Cyberpunk 2077**. desarrollado con Flask para el backend y HTML/CSS/JavaScript para el frontend. Permite simular el funcionamiento de un taxímetro real, calculando tarifas en función del estado del viaje (en movimiento o detenido).

## 🚀 Características
- 🌐 **Aplicación web con Flask**
- 🎨 **Diseño Cyberpunk 2077** con CSS personalizado
- 🔒 **Sistema de autenticación de usuarios** (registro e inicio de sesión)
- 📝 **Registro de historial de viajes** en JSON
- 🔄 **Actualización en tiempo real** con Flask-SocketIO

## 🛠️ Tecnologías Utilizadas
- **Backend:** Flask, Flask-SocketIO, Flask-Login
- **Frontend:** HTML, CSS, JavaScript
- **Base de datos:** JSON (posible futura migración a SQLite o PostgreSQL)

## 📂 Estructura del Proyecto
```
/taxi_prueba
│── /static
│   ├── /css (Estilos CSS)
│   ├── /fonts (Fuentes personalizadas)
│   ├── /js (Scripts)
│── /templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│── /data
│   ├── historial.json
│   ├── users.json
│── app.py
│── models.py
│── requirements.txt
│── README.md
```

## 📥 Instalación y Uso
### 🔧 **1. Clonar el repositorio**
```bash
git clone https://github.com/DarthVada36/galactic_taximeter.git
cd taximetro-cyberpunk
```

### 🛠️ **2. Crear un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
```

### 📦 **3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 🚀 **4. Ejecutar la aplicación**
```bash
python app.py
```
Visita [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador.

## Uso

### Botones y funciones

- **Iniciar Viaje:** Comienza el viaje y cambia el estado a MOVIMIENTO.
- **Parar/Seguir:** Alterna entre MOVIMIENTO y PARADO.
- **Finalizar Viaje:** Termina el viaje y guarda el historial.

### Estados 

- **PARADO:** El taxi está detenido y se usa la tarifa de espera.
- **MOVIMIENTO:** El taxi está en marcha y se usa la tarifa de recorrido.

## Mejoras futuras

- Implementar una base de datos en lugar de archivos JSON.
- Agregar múltiples opciones de personalización de tarifas.
- Crear una versión web completamente responsiva.

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. Puedes usarlo y modificarlo libremente.

---
💾 **Desarrollado por:** *DarthVada36* | 🚀 *Cyberpunk Taxi System*
**Proyecto desarrollado con ❤️ y mucha inspiración Cyberpunk.**


# 🚕 Taxímetro Digital - Cyberpunk 2077 Style

## 📌 Descripción
Este es un **taxímetro digital** inspirado en el universo de **Cyberpunk 2077**. Permite a los conductores calcular tarifas en función del tiempo y el movimiento del vehículo, registrando el historial de viajes. La interfaz está diseñada con una estética futurista y cuenta con autenticación de usuario para mayor seguridad.

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
git clone https://github.com/tuusuario/taximetro-cyberpunk.git
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

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. Puedes usarlo y modificarlo libremente.

---
💾 **Desarrollado por:** *Tu Nombre o Usuario* | 🚀 *Cyberpunk Taxi System*


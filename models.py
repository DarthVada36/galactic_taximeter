from flask_login import UserMixin
from flask_bcrypt import Bcrypt
import json
import os

bcrypt = Bcrypt()

USERS_FILE = "data/users.json"

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Cargar usuarios desde JSON
def load_users():
    """Carga los usuarios desde el archivo JSON."""
    if not os.path.exists(USERS_FILE):  # Si el archivo no existe, crearlo vacío
        save_users({})  # Guarda un diccionario vacío en users.json
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if not isinstance(data, dict):  # Asegurar que es un diccionario
                return {}
            return data
        except json.JSONDecodeError:  # Si el archivo está mal formateado
            return {}  # Devuelve un diccionario vacío en lugar de fallar

# Guardar usuarios en JSON
def save_users(users):
    """Guarda los usuarios en el archivo JSON."""
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

# Registrar un nuevo usuario
def register_user(username, password):
    """Registra un usuario nuevo en el sistema."""
    users = load_users()

    if username in users:
        return False  # Usuario ya existe

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    user_id = str(len(users) + 1)
    
    users[user_id] = {
        "username": username,
        "password": hashed_password
    }
    save_users(users)
    return True  # Registro exitoso

# Autenticar usuario
def authenticate_user(username, password):
    users = load_users()
    
    for user_id, user in users.items():
        if user["username"] == username and bcrypt.check_password_hash(user["password"], password):
            return User(user_id, username, user["password"])  # Usuario autenticado
    
    return None  # Credenciales incorrectas

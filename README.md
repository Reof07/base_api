### 1. Clonar el repositorio
```bash
git clone https://github.com/xxxxx/xxxxx
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
```

### 3. Activar el entorno virtual

1. Windows (CMD)
```bash
    venv\Scripts\activate
```
2. Windows (PowerShell):
```bash
.\venv\Scripts\activate
```
3. Linux/macOS:
```bash
source venv/bin/activate
```

### 4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno


### 6. Migrar la base de datos (si es necesario)

```bash
alembic upgrade head
```

### 7. Ejecutar la aplicación

1. development:
```bash
uvicorn main:app --reload || uvicorn app.main:app --reload
```

2. Production:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```
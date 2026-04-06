# Weather Wrapper API

Este microservicio es un "wrapper" de la API pública de Open-Meteo, exponiendo un endpoint con datos meteorológicos transformados a diferentes unidades (Fahrenheit, m/s).

## 🚀 Tecnologías Utilizadas

- **Python 3.11**
- **FastAPI**: Framework web.
- **httpx**: Cliente HTTP asíncrono.
- **PyTest**: Framework de pruebas unitarias.
- **Docker**: Contenedorización.

## 📋 Prerrequisitos

- Docker instalado.
- (Opcional) Python 3.11+ instalado para desarrollo local.

## 🛠️ Instalación y Configuración

### 1. Desarrollo Local (con entorno virtual)

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Linux/macOS

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar Tests

```bash
pytest tests/test_weather_service.py
```

### 3. Levantar la Aplicación Localmente

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## 🐳 Uso con Docker

### 1. Construir la imagen

```bash
docker build -t weather-wrapper .
```

### 2. Ejecutar el contenedor

```bash
docker run -p 8000:8000 weather-wrapper
```

## 📡 Endpoint Principal

### GET `/api/v1/weather-summary`

Devuelve un resumen del clima actual para una ubicación fija (Valencia, España).

**Ejecución de ejemplo (cURL):**
```bash
curl http://localhost:8000/api/v1/weather-summary
```

**Respuesta de ejemplo:**
```json
{
  "temperature": {
    "celsius": 20.5,
    "fahrenheit": 68.9
  },
  "wind_speed": {
    "kmh": 12.0,
    "ms": 3.33
  },
  "metadata": {
    "datetime": "2024-04-06T14:10:00.000000",
    "latitude": 39.47,
    "longitude": -0.38
  }
}
```

## 📄 Archivos del Proyecto

- `src/main.py`: Punto de entrada de FastAPI.
- `src/weather_service.py`: Lógica de negocio y transformaciones.
- `tests/test_weather_service.py`: Pruebas de unidad.
- `Dockerfile`: Configuración del contenedor.
- `requirements.txt`: Dependencias del proyecto.
- `GEMINI_CONTEXT.md`: Contexto y estado del proyecto.

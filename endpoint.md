Actúa como un Desarrollador Senior de Backend. Necesito que crees un microservicio que exponga una API REST con un único endpoint de consulta meteorológica. El objetivo es actuar como un "wrapper" procesado de una API externa.

1. Especificaciones del Origen de Datos

El servicio debe consumir datos de la siguiente URL (Open-Meteo):
https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.38&current_weather=true

2. Requerimientos del Endpoint

Crea un endpoint GET (por ejemplo, /api/v1/weather-summary) que devuelva un JSON con la siguiente estructura y transformaciones:

Temperatura: Debe mostrarse en grados Celsius (°C) y en Fahrenheit (°F).

Velocidad del viento: Debe mostrarse en km/h y en m/s.

Metadatos: Incluir la fecha/hora de la consulta y las coordenadas utilizadas.

3. Arquitectura y Calidad de Código

Transformaciones: Implementa métodos independientes para las conversiones de unidades (Celsius a Fahrenheit y Km/h a m/s).

Testing: Es obligatorio incluir tests unitarios para todos los métodos de transformación y para la lógica de formateo de la respuesta. Utiliza un framework de pruebas estándar (como Jest para Node.js, PyTest para Python o JUnit para Java).

Manejo de Errores: Implementa un control básico para gestionar posibles fallos en la llamada a la API externa.

4. Stack Tecnológico

Usa Python con FastAPI.

Por favor, entrega el código del servidor, la lógica de negocio y el archivo de tests.

# Azure Service Bus - Productor y Consumidor

Este proyecto demuestra cómo enviar y recibir mensajes desde una cola de Azure Service Bus usando Python.

## 🎯 Tema del Proyecto: Gestión de Incidentes en una Universidad

### 📝 Descripción del Caso de Uso

En una universidad, los estudiantes, docentes o personal administrativo pueden reportar incidentes como:

- Problemas con infraestructura (luces dañadas, puertas rotas, etc.)
- Fallos en sistemas informáticos (plataforma virtual caída, problemas de acceso)
- Emergencias médicas o de seguridad

Para manejar estos reportes de forma eficiente y desacoplada, se utiliza un Enterprise Service Bus (ESB) con Azure Service Bus. Así, los sistemas que generan los reportes (por ejemplo, una app móvil o un portal web) pueden enviar mensajes a una cola, y otros sistemas (como el sistema de gestión de mantenimiento o seguridad) pueden consumirlos y actuar en consecuencia.

## 📁 Estructura

- `producer.py`: Envía mensajes a la cola.
- `consumer.py`: Escucha y procesa mensajes.
- `config.json`: Contiene las credenciales de conexión.
- `requirements.txt`: Dependencias del proyecto.

## 🚀 Uso

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
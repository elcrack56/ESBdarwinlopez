import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from datetime import datetime

with open("C:/JSONS/conexion.json") as f:
    config = json.load(f)

connection_str = config["connection_string_send"]
queue_name = config["queue_name"]

print("Bienvenido al sistema de reporte de incidentes de esta Universidad.")
print("Selecciona el tipo de incidente:")
print("1. Arquitectura (infraestructura)")
print("2. Sistemas (tecnología)")
opcion = input("Opción (1 o 2): ")

if opcion == "1":
    tipo = "Arquitectura"
    descripcion = input("Describe el problema de infraestructura: ")
elif opcion == "2":
    tipo = "Sistemas"
    descripcion = input("Describe el problema del sistema: ")
else:
    print("Opción inválida.")
    exit()

incident_message = {
    "tipo": tipo,
    "descripcion": descripcion,
    "prioridad": "Media",
    "reportado_por": input("Usuario que reporta: "),
    "fecha": datetime.now().isoformat()
}

with ServiceBusClient.from_connection_string(connection_str) as client:
    sender = client.get_queue_sender(queue_name=queue_name)
    with sender:
        message = ServiceBusMessage(json.dumps(incident_message))
        sender.send_messages(message)
        print("✅ Mensaje enviado correctamente.")


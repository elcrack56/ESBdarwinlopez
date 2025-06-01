import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from datetime import datetime

with open("C:/JSONS/conexion.json") as f:
    config = json.load(f)

connection_str = config["CONNECTION_STR_SEND"]
queue_name = config["QUEUE_NAME"]

print("Bienvenido al sistema de reporte de incidentes de esta Universidad.")
print("Selecciona el tipo de incidente:")
print("1. Arquitectura (infraestructura)")
print("2. Sistemas (tecnología)")
print("3. Emergencia medicas (salud)")
print("4. Emergencia de Seguridad (Control de acceso, Personal de seguridad)")
opcion = input("Escribe el numero de cualquier opcion que te muestra el menu: ")

if opcion == "1":
    tipo = "Arquitectura"
    descripcion = input("Describe el problema de infraestructura: ")
    prioridad = input("Prioridad del incidente (Alta, Media, Baja): ")
elif opcion == "2":
    tipo = "Sistemas"
    descripcion = input("Describe el problema del sistema: ")
    prioridad = input("Prioridad del incidente (Alta, Media, Baja): ")
elif opcion == "3":
    tipo = "Emergencia Medica"
    descripcion = input("Describe la emergencia médica: ")
    prioridad = input("Prioridad del incidente (Alta, Media, Baja): ")
elif opcion == "4":
    tipo = "Emergencia de Seguridad"
    descripcion = input("Describe la emergencia de seguridad: ")
    prioridad = input("Prioridad del incidente (Alta, Media, Baja): ")
else:
    print("Opción inválida.")
    exit()

incident_message = {
    "tipo": tipo,
    "descripcion": descripcion,
    "prioridad": prioridad,
    "reportado_por": input("Usuario que reporta: "),
    "fecha": datetime.now().isoformat()
}

with ServiceBusClient.from_connection_string(connection_str) as client:
    sender = client.get_queue_sender(queue_name=queue_name)
    with sender:
        message = ServiceBusMessage(json.dumps(incident_message))
        sender.send_messages(message)
        print("✅ Mensaje enviado correctamente.")


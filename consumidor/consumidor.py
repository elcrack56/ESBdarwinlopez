import json
from azure.servicebus import ServiceBusClient

with open("C:/JSONS/conexion.json") as f:
    config = json.load(f)

connection_str = config["CONNECTION_STR_LISTEN"]
queue_name = config["QUEUE_NAME"]

with ServiceBusClient.from_connection_string(connection_str) as client:
    receiver = client.get_queue_receiver(queue_name=queue_name, max_wait_time=5)
    with receiver:
        for msg in receiver:
            try:
                body = str(msg)
                if body.strip():
                    incident = json.loads(body)
                    print(f"✅ Mensaje recibido: {incident}")
                else:
                    print("⚠️ Mensaje vacío recibido.")
                receiver.complete_message(msg)
            except json.JSONDecodeError as e:
                print(f"❌ Error al decodificar el mensaje: {e}")


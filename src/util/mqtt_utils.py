import paho.mqtt.client as mqtt
import random
import time
from util.variables import logger
from util.utils import CONFIG_DIR
from util.config_utils import get_mqtt_env


def mqtt_connector():
    logger.info('Connecting to mqtt server')
    host, port, client = get_mqtt_env()
    client_conn = mqtt.Client(client)
    client_conn.connect(host, port)
    return client_conn


def conectado(cliente, userdata, flags, rc):
    if rc == 0:
        logger.info('Cliente conectado OK')
        cliente.subscribe('demo')
    else:
        logger.info('El cliente no se pudo conectar')


def receptor(cliente, userdata, mensaje):
    logger.info(mensaje.payload)


def mqtt_suscribe():
    client_conn = mqtt_connector()
    client_conn.on_connect = conectado
    client_conn.on_message = receptor

    client_conn.loop_forever()
    logger.info("Finish program")


def example_publish():
    client_conn = mqtt_connector()
    for i in range(50):
        data = random.randint(0, 100)
        client_conn.publish('demo', data)
        time.sleep(2)

    print('Fin del programa')
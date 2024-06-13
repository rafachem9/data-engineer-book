import socket
import threading as th
from util.variables import logger
from util.config_utils import get_sockets_env


def bind_socket():
    logger.info('Creando servidor socket')
    s = socket.socket()
    host, port = get_sockets_env()
    s.bind((host, port))
    s.listen(10)
    return s


def manage_socket_connection(sc, addrc):
    logger.info(f"Cliente conectado: {addrc}")
    continuar = True
    while continuar:
        # Bytes que puede enviar el cliente
        dato = sc.recv(64)
        if not dato:
            continuar = False
            logger.info(f"Cliente {addrc} se ha desconectado")
        else:
            logger.info(f"Cliente {addrc} ha enviado {dato}")
    sc.close()


def create_socket():
    s = bind_socket()
    logger.info("Esperando conexion...")
    (sc, addrc) = s.accept()
    manage_socket_connection(sc, addrc)
    s.close()
    logger.info("Finish program")


def create_socket_thread():
    s = bind_socket()
    logger.info("Esperando conexion...")
    while True:
        (sc, addrc) = s.accept()
        hilo = th.Thread(target=manage_socket_connection, args=(sc, addrc))
        hilo.start()
    s.close()
    logger.info("Finish program")


def connect_socket():
    logger.info('Connecting to socket server')

    s = socket.socket()
    host, port = get_sockets_env()
    s.connect((host, port))
    logger.info('Connect server')
    continuar = True

    while continuar:
        dato = input("Escribe un mensaje al Servidor: ")
        if dato == "z":
            continuar = False
        else:
            s.send(dato.encode())
    s.close()
    logger.info("Finish program")


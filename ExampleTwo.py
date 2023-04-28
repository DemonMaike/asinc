# Здесь попробую реализовать самый простой асинхронный вариант решения

import socket
from select import select # импорт стандартной функции, которая следит за состояниями объектов

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_socket.bind(('localhost', 5000)) # На этом этапе мы создаём файл сокета, который обладает файловым дискриптором, на основе этого можем воспользоваться select
server_socket.listen() 


def accept_connection(server_socket): # Разделяем и формируем функцию на создание подключения
    client_socket, addr = server_socket.accept() 
    print('Connection from', addr)
    to_monitor.append(client_socket)



def send_of_client(client_socket): # Разделяем и формируем функцию на отправку сообщения 
    request = client_socket.recv(4096) 
    
    if request:
        response = 'Hello World!\n'.encode() 
        client_socket.send(response)
    else:
        server_socket.close() 


def event_loop(): # формируем менеджер задач
    while True:
        print(to_monitor) 
        ready_to_read, _, _ = select(to_monitor, [], []) # здесь происходит контроль сокетов, добовляем список в мониторинг
        
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_of_client(sock)
    


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
      
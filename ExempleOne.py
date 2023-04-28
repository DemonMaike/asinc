import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаём сокет, тип адресов ipv4, используем протокол TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # настройка сокета, включаем перееиспользование, т.к. по стандарту сокет будет занят какое то время, чтобы идущие пакеты успели дойти
server_socket.bind(('localhost', 5000)) # привязываем сокет к хосту
server_socket.listen() # включаем сокет на прослушивание


while True: # сервер постоянно слушает вход
    client_socket, addr = server_socket.accept() # мы начинаем следить за приходящими подключениями, данный метод выдает кортеж входящих подключений, сокет и адрес
    print('Connection from', addr)
    
    while True: # постоянно проверяем, получили мы что то, если нет, прерываем эту часть цикла, если получили запрос - выдаем ответ и дальше опять брейк.
        request = client_socket.recv(4096) # принемаем запрос пользователя, указываем буфер для сообщения - 4 кб
        
        if not request:
            break
        else:
            response = 'Hello World!\n'.encode() # если есть запрос, оттдаем ответ, всё передается в байтах, по этому кодируем в байты.
            client_socket.send(response) # ответ
            
    
    